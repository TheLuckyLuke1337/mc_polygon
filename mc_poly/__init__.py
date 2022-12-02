from .application import Application


def generate_and_display_trace(n, L, rotation = 0):
    app = Application(n, L, rotation)
    app.run()
