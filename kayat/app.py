# import modules
from .window import Window

class App:
    def __init__(self, title="Kayat App"):
        self.title = title
        self.window = Window(title=title)

    def run(self):
        print(f"Running {self.title}...")
        self.window.show()
        # Add your application logic here