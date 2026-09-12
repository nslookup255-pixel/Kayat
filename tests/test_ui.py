import unittest

from kayat import Component
from kayat.ui import Button, Column, Container, Row, Text


class Child(Component):
	def render(self):
		return Text("child")


class UITest(unittest.TestCase):
	def test_text_stores_its_value(self):
		text = Text("Hello", visible=True)
		self.assertEqual(text.value, "Hello")
		self.assertTrue(text.props["visible"])

	def test_button_triggers_click_callback(self):
		calls = []
		button = Button("Save", on_click=lambda value: calls.append(value))
		self.assertIsNone(button.click("done"))
		self.assertEqual(calls, ["done"])

	def test_row_and_column_keep_children_in_order(self):
		first, second = Text("first"), Text("second")
		self.assertEqual(Row(first, second).children, [first, second])
		self.assertEqual(Column(first, second).children, [first, second])

	def test_container_accepts_layout_properties_and_nested_elements(self):
		tree = Container(
			Column(Row(Text("A"), Button("B"))),
			padding=20,
			margin=4,
			width=200,
		)
		self.assertEqual(tree.props, {"padding": 20, "margin": 4, "width": 200})
		self.assertEqual(
			[node.value if isinstance(node, Text) else node.label for node in tree.walk()],
			["A", "B"],
		)

	def test_elements_can_contain_components(self):
		child = Child()
		tree = Column(child)
		self.assertEqual(list(tree.walk()), [child])

	def test_invalid_children_are_rejected(self):
		with self.assertRaisesRegex(TypeError, "Element or Component"):
			Column("not a UI node")


if __name__ == "__main__":
	unittest.main()
