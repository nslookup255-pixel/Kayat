import unittest

from kayat.app import App
from kayat.ui import Component, Text


class Root(Component):
	def __init__(self):
		super().__init__()
		self.calls = []

	def render(self):
		return Text("root")

	def on_mount(self):
		self.calls.append("mount")

	def on_unmount(self):
		self.calls.append("unmount")


class AppTest(unittest.TestCase):
	def test_mount_registers_and_mounts_root_component(self):
		app = App("Test")
		root = Root()

		self.assertIs(app.mount(root), root)
		self.assertIs(app.root, root)
		self.assertTrue(app.mounted)
		self.assertTrue(root.mounted)
		self.assertEqual(root.calls, ["mount"])

	def test_run_requires_a_root_component(self):
		with self.assertRaisesRegex(RuntimeError, "without a root Component"):
			App().run()

	def test_run_does_not_remount_an_already_mounted_root(self):
		app = App()
		root = Root()
		app.mount(root)

		self.assertIs(app.run(), root)
		self.assertEqual(root.calls, ["mount"])

	def test_unmount_clears_root_and_forwards_lifecycle(self):
		app = App()
		root = Root()
		app.mount(root)

		app.unmount()

		self.assertIsNone(app.root)
		self.assertFalse(app.mounted)
		self.assertFalse(root.mounted)
		self.assertEqual(root.calls, ["mount", "unmount"])

	def test_mount_requires_a_component(self):
		with self.assertRaisesRegex(TypeError, "requires a Component"):
			App().mount(Text("not a component"))


if __name__ == "__main__":
	unittest.main()