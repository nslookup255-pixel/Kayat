<div align="center">

# Kayat

### A Python-first desktop GUI framework powered by HTML and CSS.
<image src="assets/logo.png" alt="Kayat Logo" width="200">

</div>

<p>
  <strong>Build desktop applications with Python — without writing HTML or CSS.</strong>
</p>

<p>
  <a href="#-quick-start">Quick Start</a>
  ·
    <a href="#features">Features</a>
  ·
    <a href="#documentation">Documentation</a>
    ·
    <a href="#roadmap">Roadmap</a>
</p>

<p>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/status-development-orange" alt="Development">
</p>

</div>

---

## About

**Kayat** is a Python-first desktop GUI framework that lets you build graphical applications using Python.

Instead of writing HTML and CSS directly, you build your interface with Kayat's Python components. Kayat handles the rendering layer internally.

<!-- Put a screenshot of a Kayat application here -->

> **Python in. Desktop app out.**

---

## Features

<table>
<tr>
<td width="50%">

### Python-first

Build your application and UI using Python.

No need to manually write HTML or CSS.

</td>
<td width="50%">

### Component-based

Build interfaces by composing reusable components.

```python
Column(
    Text("Hello"),
    Button("Click me")
)
```

</td>
</tr>

<tr>
<td>

### Reactive State

Manage application state and update your UI when state changes.

</td>
<td>

### Events

Handle user interactions directly from Python.

```python
Button(
    "Click me",
    on_click=handle_click
)
```

</td>
</tr>

<tr>
<td>

### HTML-powered

Kayat uses HTML and CSS internally to render the user interface.

</td>
<td>

### Desktop GUI

Create desktop applications while keeping your development workflow Python-based.

</td>
</tr>

<tr>
<td>

### Dialogs

Use built-in alert, confirmation, and user input dialogs.

</td>
</tr>
</table>

---

# 🚀 Quick Start

## 📦 Installation

```bash
pip install kayat
```

> Kayat is currently under active development.
> The first PyPI release is planned for v0.2.0.

## Hello, Kayat!

```python
from kayat import App
from kayat.ui import Column, Text, Button


def hello():
    print("Hello from Kayat!")


app = App(
    title="Hello Kayat",
    content=Column(
        Text("Hello, Kayat!"),
        Button("Click me", on_click=hello)
    )
)

app.run()
```

<!-- Put a GIF/video screenshot of the Hello Kayat app here -->

<div align="center">

**That's it.**

</div>

---

# Components

Kayat uses a component-based UI model.

```python
Column(
    Text("Welcome to Kayat"),
    Button("Get Started"),
    Row(
        Button("Settings"),
        Button("About")
    )
)
```

A UI can be composed into a tree:

```text
Column
├── Text
├── Button
└── Row
    ├── Button
    └── Button
```

This makes it possible to build complex interfaces from small, reusable components.

<!-- Put a component tree / UI screenshot here -->

---

# State & Events

Kayat provides built-in systems for application state and user interaction.

### State

```python
from kayat.core.state import State


class Counter:
    count = State(0)
```

### Events

```python
Button(
    "Increment",
    on_click=increment
)
```

State and events are designed to work together so applications can respond to user interaction.

<!-- Put a state/event demonstration GIF here -->

---

# UI Without HTML

Kayat is powered by HTML and CSS internally.

However, you don't have to build your UI by writing HTML manually.

Instead of:

```html
<div class="container">
    <span>Hello</span>
    <button>Click me</button>
</div>
```

you can write:

```python
Column(
    Text("Hello"),
    Button("Click me")
)
```

Kayat transforms the component tree into the underlying UI representation.

---

# How It Works

```text
┌─────────────────────┐
│  Python Application │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Kayat Components  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    HTML Renderer    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      HTML / CSS     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       WebView       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Desktop Window    │
└─────────────────────┘
```

<!-- Put architecture diagram image here -->

Kayat separates application logic from the rendering layer, allowing developers to work primarily with Python.

---

# Example

<!-- Put a large screenshot of a more complete Kayat application here -->

<div align="center">

*Example application built with Kayat*

</div>

---

# Deployment

One of Kayat's goals is to make desktop application distribution simple.

The planned workflow is:

```text
Kayat Project
      │
      ▼
   kayat build
      │
      ▼
Desktop Application
```

Planned deployment features include:

* [ ] Application packaging
* [ ] Standalone executable builds
* [ ] Cross-platform builds
* [ ] Simple project configuration
* [ ] CLI build tools

---

## Roadmap

Kayat is a Python-first GUI framework designed to integrate naturally with existing Python applications and libraries, while making GUI development and deployment simple.

### v0.2 — Foundation

Focus on making the core Kayat API usable and stable.

- Python ↔ JavaScript communication
- WebView integration
- Window management improvements
- Dialogs
- Assets management
- Custom application icons
- Simplified public API
- Python function ↔ event integration
- Support for arbitrary Python values in State
- Basic value → UI representation

### v0.3 — Developer Experience

Focus on making it easy to start a Kayat project.

- `kayat new <project-name>`
- Project scaffolding
- Virtual environment setup
- Dependency detection
- Dependency installation/setup
- `kayat dev`
- Development server
- Hot reload
- Better error messages

`kayat new` will eventually be able to inspect an existing Python project, detect its dependencies, create and configure a virtual environment, and set up the required project dependencies.

### v0.4 — Integration

Focus on integration with the existing Python ecosystem.

- Arbitrary Python object support
- External function result integration
- Iterable result handling
- Async function support
- Custom renderer API
- Python object → UI conversion
- File/image data integration
- JSON/list/dict representations
- Examples integrating common Python libraries

### v0.5 — Development Workflow

Focus on improving the day-to-day development experience.

- Improved dependency detection
- Project configuration
- Environment/version checks
- Debugging improvements
- Better development tooling
- More robust error reporting

### v0.6+ — Deployment

Focus on making applications easy to distribute.

- Application packaging
- Standalone builds
- Dependency bundling
- Asset bundling
- Windows deployment
- macOS deployment
- Linux deployment
- Custom application icons


---

# Documentation

Documentation is currently being developed.

<!-- Put documentation website screenshot/image here -->

* **Getting Started**
* **Components**
* **State**
* **Events**
* **Rendering**
* **Deployment**
* **API Reference**

> Documentation will expand as the API stabilizes.

---

# Contributing

Contributions, ideas, bug reports, and discussions are welcome.

If you want to contribute:

```bash
git clone https://github.com/nslookup255-pixel/Kayat.git
cd Kayat
```

Then install the development dependencies and run the tests.

Before opening a pull request, please make sure that existing tests pass.

---

# Why "Kayat"?

The name **Kayat** comes from **Kaya Toast**, a popular Singaporean toast dish.

<!-- Put Kaya Toast image here -->

<div align="center">

**Yes, the framework is named after toast.**

</div>

---

# License

Kayat is released under the **MIT License**.

See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

<!-- Put Kayat logo image here -->

### Kayat

**Build desktop applications with Python.**

<p>
  <sub>Made with Python • HTML • CSS</sub>
</p>

</div>
