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
    │   │   └── component_name.py ...
    │   │
    │   ├── webview/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── pywebview.py
    │   │
    │   ├── bridge/
    │   │   ├── __init__.py
    │   │   ├── bridge.py
    │   │   └── js.py   
    │   │
    │   └── rendering/
    │       ├── __init__.py
    │       └── html.py
    │
    ├── examples/
    │   └── hello.py
    │
    ├── tests/
    │   └── test_name.py ...
    │
    ├── .github/
    │   └── dependabot.yml
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
- [x] Connect Python and JS