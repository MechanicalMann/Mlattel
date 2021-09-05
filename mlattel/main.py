from mlattel.display.console import ConsoleDisplay
from mlattel.app import App
from mlattel.input import KeyboardInput


def main():
    input = KeyboardInput()
    display = ConsoleDisplay()
    app = App(input, display)
    app.run()