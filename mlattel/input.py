from abc import ABC, abstractmethod
import keyboard


class Input(ABC):
    def __init__(self) -> None:
        self.on_press_score = lambda *args: None
        self.on_release_score = lambda *args: None
        self.on_press_sound = lambda *args: None
        self.on_press_start = lambda *args: None
        self.on_press_next = lambda *args: None

    @abstractmethod
    def listen(self):
        pass


class KeyboardInput(Input):
    def on_press(self, key: keyboard.KeyboardEvent):
        if key.name == 's':
            self.on_press_score()
        elif key.name == 'a':
            self.on_press_sound()
        elif key.name == 'n':
            self.on_press_next()
        elif key.name == 'space':
            self.on_press_start()

    def on_release(self, key: keyboard.KeyboardEvent):
        if key.name == 's':
            self.on_release_score()

    async def listen(self):
        keyboard.on_press(self.on_press)
        keyboard.wait('ctrl+c')