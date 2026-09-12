from ..core.element import Element


class Button(Element):
	"""A clickable leaf element."""

	def __init__(self, label, on_click=None, **props):
		super().__init__(on_click=on_click, **props)
		self.label = label

	def click(self, *args, **kwargs):
		return self.trigger("click", *args, **kwargs)
