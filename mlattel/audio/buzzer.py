from mlattel.blaseball.types import EventType
import time
import RPi.GPIO as GPIO
from mlattel.blaseball.events import GameEvent
from . import Audio

BUZZER = 12
DUTY_CYCLE = 50


class Buzzer(Audio):
    def __init__(self) -> None:
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUZZER, GPIO.OUT)

        self.tone = GPIO.PWM(BUZZER, 50)

    def startup(self):
        self._play([(262, 1), (0, 1), (523, 1), (440, 1), (392, 1), (330, 1),
                    (392, 3), (294, 3)], 0.3)

    def shutdown(self):
        self._play([(370, 1), (392, 1), (440, 3), (492, 3), (523, 1), (392, 1),
                    (330, 1), (262, 1)], 0.3)

    def handle(self, event: GameEvent):
        if event.type == EventType.STRIKE:
            self._play([(220, 1)], 0.1)
        elif event.type == EventType.BALL:
            self._play([(311, 1)], 0.1)
        elif event.type == EventType.WALK:
            self._play([(311, 1), (440, 1)], 0.1)
        elif event.type == EventType.STRIKEOUT:
            self._play([(220, 1), (156, 1)], 0.1)
        elif event.type == EventType.GROUNDOUT:
            self._play([(233, 1), (0, 1), (233, 1), (0, 1), (165, 1)], 0.1)
        elif event.type == EventType.FLYOUT:
            self._play([(784, 1), (1047, 1), (185, 1)], 0.1)
        elif event.type == EventType.HOME_RUN:
            self._play([(262, 1), (330, 1), (392, 1), (523, 1)], 0.2)
        elif event.type == EventType.HIT:
            self._play([(262, 1), (330, 1)], 0.1)
        elif event.type == EventType.FOUL:
            self._play([(262, 1), (185, 1)], 0.1)
        elif event.type == EventType.END_OF_INNING:
            self._play([(392, 1), (330, 1), (262, 1)], 0.2)
        elif event.type == EventType.INNING_CHANGE and event.prev and not event.prev.type == EventType.END_OF_INNING:
            self._play([(392, 1), (330, 1)], 0.2)

    def _play(self, notes, tempo=1.0):
        if not self.enabled:
            return
        self.tone.start(DUTY_CYCLE)
        for note, beat in notes:
            if note > 0.0:  # 0 is for rests
                self.tone.ChangeDutyCycle(DUTY_CYCLE)
                self.tone.ChangeFrequency(note)
            else:
                self.tone.ChangeDutyCycle(0)
            time.sleep(beat * tempo)
        self.tone.ChangeDutyCycle(0)
        self.tone.stop()
