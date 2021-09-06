import keyboard
from . import Input


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