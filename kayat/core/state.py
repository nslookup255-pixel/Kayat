from kayat.core.events import Events

class State:

    def __init__(self):
        self._data = {}
        self._events = Events()

    def get(self, key):
        if key not in self._data:
            raise KeyError(key)
        return self._data.get(key)

    def set(self, key, value):
        old_value = self._data.get(key)

        if old_value == value and key in self._data:
            return

        self._data[key] = value
        self._events.emit("change", key, old_value, value)

    def on(self, key, callback):
        self._events.on(key, callback)

    def off(self, key, callback):
        self._events.off(key, callback)

    def delete(self, key):
        if key in self._data:
            old_value = self._data.get(key)
            del self._data[key]
            self._events.emit("change", key, old_value, None)