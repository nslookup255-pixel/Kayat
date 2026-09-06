from kayat import App

app = App("Hello Kayat")

app.window.load_html("""
<h1>Hello, Kayat!</h1>
<p>This is a simple example of a Kayat application.</p>
""")

app.run()