from .core.bridge import Bridge
from .core.js import JS
from .webview.pywebview import PyWebView


class PythonAPI:
    def __init__(self, bridge):
        self._bridge = bridge

    def call(self, name, *args, **kwargs):
        return self._bridge.call(name, *args, **kwargs)


class Window:
    def __init__(self, title="Kayat App", width=800, height=600):
        self.title = title
        self.width = width
        self.height = height

        self.bridge = Bridge()
        self.api = PythonAPI(self.bridge)

        self.webview = PyWebView(
            title,
            width,
            height,
            self.api,
        )
        self.js = JS(self.webview)

    def load_html(self, html):
        self.webview.load_html(html)

    def show(self):
        self.webview.show()

    def close(self):
        self.webview.close()