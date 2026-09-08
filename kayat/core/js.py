class JS:
    def __init__(self, bridge):
        self._bridge = bridge

    def call(self, name, *args):
        return self._bridge.call("js_call", name, *args)