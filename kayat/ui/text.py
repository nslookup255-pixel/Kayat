from ..core.element import Element


class Text(Element):
	"""A leaf element that stores displayable text or another simple value."""

	def __init__(self, value, **props):
		super().__init__(**props)
		self.value = value
