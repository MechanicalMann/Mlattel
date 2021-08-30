from mlattel.app import App
from mlattel.input import KeyboardInput


def main():
    input = KeyboardInput()
    app = App(input)
    app.run()