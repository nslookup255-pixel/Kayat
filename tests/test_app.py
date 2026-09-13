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


class FakeWindow:
	def __init__(self):
		self.loaded_html = []
		self.show_calls = 0

	def load_html(self, html):
		self.loaded_html.append(html)

	def load(self, html):
		self.load_html(html)

	def show(self):
		self.show_calls += 1


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
		window = FakeWindow()
		app = App(window=window)
		root = Root()
		app.mount(root)

		self.assertIs(app.run(), root)
		self.assertEqual(root.calls, ["mount"])
		self.assertEqual(window.show_calls, 1)

	def test_run_renders_root_and_loads_html_into_window(self):
		window = FakeWindow()
		app = App("Test", width=1024, height=768, window=window)
		app.mount(Root())

		app.run()

		self.assertEqual(window.show_calls, 1)
		self.assertEqual(
			window.loaded_html,
			['<span class="kayat-text">root</span>'],
		)
		self.assertEqual((app.title, app.width, app.height), ("Test", 1024, 768))

	def test_run_loads_rendered_html_each_time_without_remounting(self):
		window = FakeWindow()
		app = App(window=window)
		app.mount(Root())

		app.run()
		app.run()

		self.assertEqual(window.show_calls, 2)
		self.assertEqual(len(window.loaded_html), 2)

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