from kayat import App, Component
from kayat.ui import Column, Text, Button


class Hello(Component):
    def render(self):
        return Column(
            Text("Hello from Kayat"),
            Button("Click"),
        )


if __name__ == "__main__":
    app = App(title="Hello from Kayat")
    app.mount(Hello())
    app.run()
