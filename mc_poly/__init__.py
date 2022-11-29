from .application import Application


def generate_and_display_trace(n, L):
    app = Application(n, L)
    app.run()
