from kayat import App, Component
from kayat.ui import Column, Text, Button


class Hello(Component):
    def render(self):
        return Column(
            Text("Welcome to Kayat!"),
            Text("This is a simple example of a Kayat app."),
            Button("Click me!"),
        )


if __name__ == "__main__":
    app = App(title="Hello from Kayat")
    app.mount(Hello())
    app.run()
