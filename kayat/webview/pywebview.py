import webview

from ..core.bridge import Bridge
from ..core.js import JS
from .base import WebView


class PyWebView(WebView):
    def __init__(self, title, width, height, bridge):
        self.title = title
        self.width = width
        self.height = height
        self.bridge = bridge
        self.html = ""
        self.js_api = JS(self.bridge)

    def load_html(self, html):
        self.html = html

    def show(self):
        self.window = webview.create_window(
            self.title,
            html=self.html,
            width=self.width,
            height=self.height,
        )

        webview.start()

    def close(self):
        self.window.destroy()