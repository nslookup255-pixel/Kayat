from .core import Component, Element, Events, State

__all__ = ["App", "Component", "Element", "Events", "State", "Window"]


def __getattr__(name):
	if name == "App":
		from .app import App

		return App
	if name == "Window":
		from .window import Window

		return Window
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
