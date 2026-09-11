class Element:
	"""A renderable UI node with child elements or components."""

	def __init__(self, *children, **props):
		self.children = list(children)
		self.props = props

	def walk(self):
		for child in self.children:
			yield from child.walk() if isinstance(child, Element) else (child,)

	def trigger(self, event_name, *args, **kwargs):
		callback = self.props.get(f"on_{event_name}")
		if callback is not None:
			return callback(*args, **kwargs)