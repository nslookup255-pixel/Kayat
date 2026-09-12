from .core.component import Component

class App:
    def __init__(self, title="Kayat App"):
        self.title = title
        self.root = None
        self._mounted = False

    @property
    def mounted(self):
        return self._mounted

    def mount(self, component):
        if not isinstance(component, Component):
            raise TypeError("App.mount() requires a Component")

        if self._mounted:
            self.unmount()

        self.root = component
        self.root.mount()
        self._mounted = True
        return self.root

    def unmount(self):
        if self.root is not None:
            self.root.unmount()

        self.root = None
        self._mounted = False

    def run(self):
        if self.root is None:
            raise RuntimeError("Cannot run an App without a root Component")

        if not self._mounted:
            self.root.mount()

        return self.root
