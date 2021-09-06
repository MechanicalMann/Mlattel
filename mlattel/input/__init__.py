from abc import ABC, abstractmethod


class Input(ABC):
    def __init__(self) -> None:
        self.on_press_score = lambda *args: None
        self.on_release_score = lambda *args: None
        self.on_press_sound = lambda *args: None
        self.on_press_start = lambda *args: None
        self.on_press_next = lambda *args: None

    def listen(self):
        pass

    def cleanup(self):
        pass