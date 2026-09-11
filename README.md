# Kayat

Build desktop GUI applications with Python and HTML.


## File Structure Diagram

    Kayat/
    ├── kayat/
    │   ├── __init__.py
    │   ├── app.py
    │   ├── window.py
    │   │
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── bridge.py
    │   │   ├── events.py
    │   │   ├── state.py
    │   │   └── js.py
    │   │
    │   ├── ui/
    │   │   ├── __init__.py
    │   │   └── component.py
    │   │
    │   └── webview/
    │       ├── __init__.py
    │       ├── base.py
    │       └── pywebview.py
    │
    ├── examples/
    │   └── hello.py
    │
    ├── tests/
    │   └── test_name.py ...
    │
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE
    └── .gitignore

## To-Do

### Implementation

- [x] Events system
- [x] State management system
- [ ] Component system <- In progress
- [ ] Element / UI
- [ ] Connect Windows and Webview(UI)
- [ ] Connect Python and JS
- [ ] Real HTML rendering