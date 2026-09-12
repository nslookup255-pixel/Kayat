class Bridge:
    def __init__(self):
        self._functions = {}

    def register(self,name,function):
        self._functions[name] = function
        return function

    def call(self, name, *args, **kwargs):
        function = self._functions.get(name)

        if function is None:
            raise ValueError(f"Unknown bridge function: {name}")

        return function(*args, **kwargs)