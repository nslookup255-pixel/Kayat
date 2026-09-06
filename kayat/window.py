class Window:
    def __init__(self, title="kayat App", width=800, height=600):
        self.title = title
        self.width = width
        self.height = height

    def show(self):
        print(f"Showing window '{self.title}' with size {self.width}x{self.height}")