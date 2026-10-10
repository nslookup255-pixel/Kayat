import os
import subprocess
import sys
import sysconfig
import unittest
from contextlib import redirect_stderr, redirect_stdout
from importlib.metadata import PackageNotFoundError, version
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from kayat.cli import main


class CLITest(unittest.TestCase):
	def test_existing_top_level_package_exports_are_available(self):
		import kayat

		for name in kayat.__all__:
			with self.subTest(name=name):
				self.assertIsNotNone(getattr(kayat, name))

	def test_help_shows_usage_description_and_supported_options(self):
		output = StringIO()
		with redirect_stdout(output), self.assertRaises(SystemExit) as exit_info:
			main(["--help"])

		self.assertEqual(exit_info.exception.code, 0)
		self.assertIn("usage: kayat", output.getvalue())
		self.assertIn("Python-first desktop GUI framework", output.getvalue())
		self.assertIn("--help", output.getvalue())
		self.assertIn("--version", output.getvalue())
		self.assertNotIn("KAYAT", output.getvalue())

	def test_version_matches_installed_package_metadata(self):
		output = StringIO()
		with redirect_stdout(output), self.assertRaises(SystemExit) as exit_info:
			main(["--version"])

		self.assertEqual(exit_info.exception.code, 0)
		self.assertEqual(output.getvalue().strip(), f"kayat {version('kayat')}")
		self.assertNotIn("KAYAT", output.getvalue())

	def test_version_reports_missing_package_metadata(self):
		error_output = StringIO()
		with (
			patch("kayat.cli.version", side_effect=PackageNotFoundError("kayat")),
			redirect_stderr(error_output),
			self.assertRaises(SystemExit) as exit_info,
		):
			main(["--version"])

		self.assertEqual(exit_info.exception.code, 2)
		self.assertIn("could not determine the installed Kayat version", error_output.getvalue())

	def test_no_arguments_prints_brand_header(self):
		output = StringIO()
		with redirect_stdout(output):
			main([])

		self.assertEqual(output.getvalue(), "KAYAT\nPython GUI Framework\n")

	def test_options_do_not_import_gui_modules(self):
		for option in ("--help", "--version"):
			with self.subTest(option=option):
				code = (
					"import sys\n"
					"from kayat.cli import main\n"
					"try:\n"
					f"    main([{option!r}])\n"
					"except SystemExit as error:\n"
					"    if error.code != 0:\n"
					"        raise\n"
					"assert not any(name == 'webview' or "
					"name.startswith('kayat.webview') or name == 'kayat.window' "
					"for name in sys.modules)\n"
				)
				result = subprocess.run(
					[sys.executable, "-c", code],
					capture_output=True,
					text=True,
					check=False,
				)

				self.assertEqual(result.returncode, 0, result.stderr)

	def test_installed_console_script_handles_help_and_version(self):
		script_name = "kayat.exe" if os.name == "nt" else "kayat"
		script = Path(sysconfig.get_path("scripts")) / script_name
		self.assertTrue(script.is_file(), f"Console script not found: {script}")

		for option in ("--help", "--version"):
			with self.subTest(option=option):
				result = subprocess.run(
					[str(script), option],
					capture_output=True,
					text=True,
					check=False,
				)
				self.assertEqual(result.returncode, 0, result.stderr)
				if option == "--help":
					self.assertIn("usage: kayat", result.stdout)
					self.assertNotIn("KAYAT", result.stdout)
				else:
					self.assertEqual(
						result.stdout.strip(),
						f"kayat {version('kayat')}",
					)
					self.assertNotIn("Python GUI Framework", result.stdout)

	def test_installed_console_script_shows_header_without_arguments(self):
		script_name = "kayat.exe" if os.name == "nt" else "kayat"
		script = Path(sysconfig.get_path("scripts")) / script_name
		result = subprocess.run(
			[str(script)],
			capture_output=True,
			text=True,
			check=False,
		)

		self.assertEqual(result.returncode, 0, result.stderr)
		self.assertEqual(result.stdout, "KAYAT\nPython GUI Framework\n")


if __name__ == "__main__":
	unittest.main()
