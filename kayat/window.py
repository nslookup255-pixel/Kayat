from .core.bridge import Bridge
from .core.js import JS
from .webview.pywebview import PyWebView


class PythonAPI:
    def __init__(self, bridge):
        self._bridge = bridge

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)

        try:
            return self._bridge._functions[name]
        except KeyError as error:
            raise AttributeError(name) from error

    def __dir__(self):
        return sorted(set(super().__dir__()) | set(self._bridge._functions))

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