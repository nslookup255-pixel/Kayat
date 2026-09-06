from .webview.pywebview import PyWebView


class Window:
    def __init__(self, title="Kayat App", width=800, height=600):
        self.title = title
        self.width = width
        self.height = height

        self.webview = PyWebView(
            title,
            width,
            height,
        )

    def load_html(self, html):
        self.webview.load_html(html)

    def show(self):
        self.webview.show()