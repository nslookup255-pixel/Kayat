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
- [x] Component system
- [x] Element / UI
- [x] Connect Windows and Webview(UI)
  - [x] Real HTML rendering
- [x] Load rendered HTML into a native WebView window
- [ ] Connect Python and JS