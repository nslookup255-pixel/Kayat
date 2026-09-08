import unittest

from kayat.core.bridge import Bridge
from kayat.core.js import JS


class RecordingBridge:
	def __init__(self, result):
		self.result = result
		self.calls = []

	def call(self, name, *args):
		self.calls.append((name, args))
		return self.result


class JSApiTest(unittest.TestCase):
	def test_call_forwards_name_and_arguments_and_returns_result(self):
		bridge = RecordingBridge(result={"ok": True})
		js = JS(bridge)

		result = js.call("window.alert", "Hello", 42)

		self.assertEqual(result, {"ok": True})
		self.assertEqual(bridge.calls, [("js_call", ("window.alert", "Hello", 42))])


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
