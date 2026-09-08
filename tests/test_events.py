from kayat.core.events import Events as E

def test_on_and_emit():
    events = E()
    called = []

    def listener(arg):
        called.append(arg)

    events.on("test_event", listener)
    events.emit("test_event", 42)

    assert called == [42]

def test_off():
    events = E()
    called = []

    def listener(arg):
        called.append(arg)

    events.on("test_event", listener)
    events.off("test_event", listener)
    events.emit("test_event", 42)

    assert called == []

def test_once():
    events = E()
    called = []

    def listener(arg):
        called.append(arg)

    events.once("test_event", listener)
    events.emit("test_event", 42)
    events.emit("test_event", 43)

    assert called == [42]

def test_clear():
    events = E()
    called = []

    def listener(arg):
        called.append(arg)

    events.on("test_event", listener)
    events.clear()
    events.emit("test_event", 42)

    assert called == []

def test_emit_passes_arg():
    events = E()
    called = []

    def listener(arg1, arg2):
        called.append((arg1, arg2))

    events.on("test_event", listener)
    events.emit("test_event", 1, 2)

    assert called == [(1, 2)]

if __name__ == "__main__":
    test_on_and_emit()
    test_off()
    test_once()
    test_clear()
    test_emit_passes_arg()
    print("All tests passed.")