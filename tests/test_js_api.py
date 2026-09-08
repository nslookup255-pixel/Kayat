import unittest

from kayat.core.bridge import Bridge
from kayat.core.js import JS


class RecordingWebView:
	def __init__(self, result):
		self.result = result
		self.scripts = []

	def evaluate_js(self, script):
		self.scripts.append(script)
		return self.result


class JSApiTest(unittest.TestCase):
	def test_call_forwards_name_and_arguments_and_returns_result(self):
		webview = RecordingWebView(result={"ok": True})
		js = JS(webview)

		result = js.call("window.alert", "Hello", 42)

		self.assertEqual(result, {"ok": True})
		self.assertEqual(webview.scripts, ['globalThis["window"]["alert"]("Hello", 42)'])

	def test_call_serializes_javascript_values(self):
		webview = RecordingWebView(result=None)
		js = JS(webview)

		js.call("window.setValue", 'quote"', 3, True, None, [1, "two"], {"enabled": False})

		self.assertEqual(
			webview.scripts,
			[
				'globalThis["window"]["setValue"]('
				'"quote\\\"", 3, true, null, [1, "two"], {"enabled": false})'
			],
		)


class BridgeTest(unittest.TestCase):
	def test_registered_function_is_called_with_arguments(self):
		bridge = Bridge()

		def add(left, right):
			return left + right

		bridge.register("add", add)

		self.assertEqual(bridge.call("add", 2, 3), 5)

	def test_calling_unknown_function_raises_value_error(self):
		bridge = Bridge()

		with self.assertRaisesRegex(ValueError, "Unknown bridge function: missing"):
			bridge.call("missing")


if __name__ == "__main__":
	unittest.main()