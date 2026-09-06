from .window import Window

class App:
    def __init__(self, title="Kayat App"):
        self.title = title
        self.window = Window(title)

    def run(self):
        self.window.show()