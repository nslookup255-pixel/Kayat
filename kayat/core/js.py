import json


class JS:
    def __init__(self, webview):
        self._webview = webview

    def call(self, name, *args):
        function = "globalThis" + "".join(
            f"[{json.dumps(part)}]" for part in name.split(".")
        )
        arguments = ", ".join(json.dumps(argument) for argument in args)
        script = f"{function}({arguments})"
        return self._webview.evaluate_js(script)