import asyncio, signal
from time import sleep
import RPi.GPIO as GPIO
from . import Input

BUTTON_START = 5
BUTTON_NEXT = 6
BUTTON_SCORE = 16
BUTTON_SOUND = 26


class GpioInput(Input):
    def __init__(self) -> None:
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON_START, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_SCORE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_SOUND, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(BUTTON_START,
                              GPIO.FALLING,
                              callback=self.handle_start,
                              bouncetime=500)
        GPIO.add_event_detect(BUTTON_NEXT,
                              GPIO.FALLING,
                              callback=self.handle_next,
                              bouncetime=250)
        GPIO.add_event_detect(BUTTON_SOUND,
                              GPIO.FALLING,
                              callback=self.handle_sound,
                              bouncetime=250)
        GPIO.add_event_detect(BUTTON_SCORE,
                              GPIO.BOTH,
                              callback=self.handle_score,
                              bouncetime=250)

    def handle_start(self, *args):
        self.on_press_start(*args)

    def handle_next(self, *args):
        self.on_press_next(*args)

    def handle_score(self, *args):
        if not GPIO.input(BUTTON_SCORE):
            self.on_press_score(*args)
        else:
            self.on_release_score(*args)

    def handle_sound(self, *args):
        self.on_press_sound(*args)

    def cleanup(self, *args):
        GPIO.cleanup()

    def listen(self):
        while True:
            sleep(1000)