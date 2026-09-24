from .core import Component, Element, Events, State
from .dialogs import alert, confirm, prompt

__all__ = [
	"App",
	"Component",
	"Element",
	"Events",
	"State",
	"Window",
	"alert",
	"confirm",
	"prompt",
]


def __getattr__(name):
	if name == "App":
		from .app import App

		return App
	if name == "Window":
		from .window import Window

		return Window
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
