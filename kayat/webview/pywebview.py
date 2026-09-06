import webview

from .base import WebView


class PyWebView(WebView):
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.html = ""

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