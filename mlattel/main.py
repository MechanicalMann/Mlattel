from mlattel.audio.buzzer import Buzzer
from mlattel.display.led import LedDisplay
from mlattel.app import App
from mlattel.input.gpio import GpioInput


def main():
    try:
        input = GpioInput()
        display = LedDisplay()
        audio = Buzzer()
        app = App(input, display, audio)
        app.run()
    except KeyboardInterrupt:
        app.stop()
        input.cleanup()