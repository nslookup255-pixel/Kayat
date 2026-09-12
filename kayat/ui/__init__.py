"""Compatibility imports for the UI primitives.

The primitives now live in :mod:`kayat.core`; they remain available here so
applications using the original public ``kayat.ui`` API continue to work.
"""

from ..core.component import Button, Column, Component, Text
from ..core.element import Element
from ..core.state import State

__all__ = ["Button", "Column", "Component", "Element", "State", "Text"]
