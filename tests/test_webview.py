import sys
import types
import unittest


class FakeWindow:
	def __init__(self):
		self.scripts = []
		self.destroyed = False

	def evaluate_js(self, script):
		self.scripts.append(script)
		return {"script": script}

	def destroy(self):
		self.destroyed = True


class FakeWebViewModule:
	def __init__(self):
		self.window = FakeWindow()
		self.created_with = None

	def create_window(self, *args, **kwargs):
		self.created_with = (args, kwargs)
		return self.window

	def start(self):
		return None


fake_webview = FakeWebViewModule()
sys.modules["webview"] = types.ModuleType("webview")
sys.modules["webview"].create_window = fake_webview.create_window
sys.modules["webview"].start = fake_webview.start

from kayat.webview.pywebview import PyWebView
from kayat.bridge import Bridge
from kayat.window import PythonAPI


class PyWebViewTest(unittest.TestCase):
	def test_window_connects_both_communication_directions(self):
		from kayat.window import Window

		window = Window("Test")
		window.bridge.register("hello", lambda name: f"Hello, {name}!")

		self.assertIs(window.webview.js_api, window.api)
		self.assertEqual(window.api.hello("World"), "Hello, World!")
		self.assertIs(window.js._webview, window.webview)

	def test_registered_bridge_function_is_exposed_directly_on_js_api(self):
		bridge = Bridge()

		def hello(name):
			return f"Hello, {name}!"

		bridge.register("hello", hello)
		api = PythonAPI(bridge)

		self.assertEqual(api.hello("World"), "Hello, World!")
		self.assertIn("hello", dir(api))

	def test_show_passes_python_api_to_pywebview(self):
		api = object()
		view = PyWebView("Test", 800, 600, api)
		view.load_html("<h1>Test</h1>")

		view.show()

		args, kwargs = fake_webview.created_with
		self.assertEqual(args, ("Test",))
		self.assertEqual(kwargs["html"], "<h1>Test</h1>")
		self.assertEqual(kwargs["width"], 800)
		self.assertEqual(kwargs["height"], 600)
		self.assertIs(kwargs["js_api"], api)

	def test_evaluate_js_and_close_delegate_to_window(self):
		view = PyWebView("Test", 800, 600)
		view.window = fake_webview.window

		self.assertEqual(view.evaluate_js("1 + 1"), {"script": "1 + 1"})
		view.close()

		self.assertTrue(fake_webview.window.destroyed)


if __name__ == "__main__":
	unittest.main()
