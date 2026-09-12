from kayat.app import App
from kayat.core.state import State
from kayat.core.component import Component
from kayat.ui import Column, Text, Button


class Counter(Component):
    count = State(0)

    def increment(self):
        self.count += 1

    def render(self):
        return Column(
            Text("Welcome to Kayat!"),
            Text(f"Count: {self.count}"),
            Button("+", on_click=self.increment),
        )


app = App()
root = app.mount(Counter())

print("root:", root)
print("element:", root.element)
print("children:", root.element.children)

for child in root.element.children:
    print("child:", child)

app.run()
