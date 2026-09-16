from kayat import App, Component
from kayat.ui import Column, Text, Button


class Hello(Component):
    def handle_click(self):
        print("Button clicked!")

    def render(self):
        return Column(
            Text("Welcome to Kayat!"),
            Text("This is a simple example of a Kayat app."),
            Button("Click me!", on_click=self.handle_click),
        )


if __name__ == "__main__":
    app = App(title="Hello from Kayat")
    app.mount(Hello())
    app.run()
