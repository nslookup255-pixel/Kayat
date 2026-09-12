import unittest

from kayat.rendering import HTMLRenderer
from kayat.ui import Button, Column, Component, Container, Element, Row, Text


class UnsupportedElement(Element):
	pass


class Greeting(Component):
	def __init__(self):
		super().__init__()
		self.render_calls = 0

	def render(self):
		self.render_calls += 1
		return Text("Hello")


class HTMLRendererTest(unittest.TestCase):
	def setUp(self):
		self.renderer = HTMLRenderer()

	def test_text_renders_as_escaped_span(self):
		self.assertEqual(
			self.renderer.render(Text("<script>alert('x')</script>")),
			'<span class="kayat-text">&lt;script&gt;alert(&#x27;x&#x27;)&lt;/script&gt;</span>',
		)

	def test_button_renders_as_button(self):
		self.assertEqual(
			self.renderer.render(Button("Click")),
			'<button class="kayat-button">Click</button>',
		)

	def test_row_renders_children_in_order(self):
		self.assertEqual(
			self.renderer.render(Row(Text("A"), Text("B"))),
			'<div class="kayat-row"><span class="kayat-text">A</span><span class="kayat-text">B</span></div>',
		)

	def test_column_renders_as_a_div(self):
		self.assertEqual(
			self.renderer.render(Column(Text("Hello"))),
			'<div class="kayat-column"><span class="kayat-text">Hello</span></div>',
		)

	def test_container_renders_as_a_div(self):
		self.assertEqual(
			self.renderer.render(Container(Text("Hello"))),
			'<div class="kayat-container"><span class="kayat-text">Hello</span></div>',
		)

	def test_nested_elements_preserve_tree_and_child_order(self):
		tree = Column(Text("Hello"), Row(Button("A"), Button("B")))
		self.assertEqual(
			self.renderer.render(tree),
			'<div class="kayat-column"><span class="kayat-text">Hello</span>'
			'<div class="kayat-row"><button class="kayat-button">A</button>'
			'<button class="kayat-button">B</button></div></div>',
		)

	def test_supported_layout_properties_render_as_style(self):
		tree = Container(
			Text("content"),
			width=200,
			height="50%",
			padding=20,
			margin=4,
			gap=8,
			alignment="center",
			visible=False,
		)
		self.assertEqual(
			self.renderer.render(tree),
			'<div class="kayat-container" '
			'style="display: none; width: 200px; height: 50%; padding: 20px; '
			'margin: 4px; gap: 8px; align-items: center">'
			'<span class="kayat-text">content</span></div>',
		)

	def test_style_values_are_escaped_as_html_attributes(self):
		html = self.renderer.render(Container(alignment='" onmouseover="bad'))

		self.assertIn('align-items: &quot; onmouseover=&quot;bad', html)
		self.assertNotIn('onmouseover="bad"', html)

	def test_callbacks_are_not_serialized(self):
		def handler():
			return None

		html = self.renderer.render(Button("Click", on_click=handler))
		self.assertNotIn("on_click", html)
		self.assertNotIn("handler", html)

	def test_component_is_mounted_and_its_element_is_rendered(self):
		component = Greeting()

		self.assertEqual(self.renderer.render(component), '<span class="kayat-text">Hello</span>')
		self.assertTrue(component.mounted)
		self.assertEqual(component.render_calls, 1)
		self.assertEqual(self.renderer.render(component), '<span class="kayat-text">Hello</span>')
		self.assertEqual(component.render_calls, 1)

	def test_disabled_button_is_marked_disabled(self):
		self.assertEqual(
			self.renderer.render(Button("Click", enabled=False)),
			'<button class="kayat-button" disabled>Click</button>',
		)

	def test_unsupported_elements_fail_predictably(self):
		with self.assertRaisesRegex(TypeError, "does not support element type UnsupportedElement"):
			self.renderer.render(UnsupportedElement())


if __name__ == "__main__":
	unittest.main()
