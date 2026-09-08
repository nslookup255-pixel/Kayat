import webview

from .base import WebView


class PyWebView(WebView):
    def __init__(self, title, width, height, js_api=None):
        self.title = title
        self.width = width
        self.height = height
        self.js_api = js_api
        self.html = ""

    def load_html(self, html):
        self.html = html

    def evaluate_js(self, script):
        return self.window.evaluate_js(script)

    def show(self):
        self.window = webview.create_window(
            self.title,
            html=self.html,
            width=self.width,
            height=self.height,
            js_api=self.js_api,
        )

        webview.start()

    def close(self):
        self.window.destroy()