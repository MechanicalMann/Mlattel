import asyncio
from mlattel.blaseball.events import EventListener, Game, GameEvent
from mlattel.input import Input


class App(EventListener):
    def __init__(self, input: Input) -> None:
        self.game = None
        self._loop = None
        self._input = input
        self._input.on_press_start = self.start
        self._input.on_press_next = self.next
        self._input.on_press_sound = self.sound
        self._input.on_press_score = self.show_score
        self._input.on_release_score = self.hide_score

    def show_score(self):
        if not self.game:
            print('No active game')
        print(f'Home: {self.game.home_score} Away: {self.game.away_score}')

    def hide_score(self):
        pass

    def start(self):
        if not self.game:
            self.game = Game('53c3e12c-5a94-49ea-9804-4358aee1edb6', self)
            self._loop = asyncio.new_event_loop()
            self._loop.run_until_complete(self.game.get_events())
        else:
            self._loop.close()
            self.game = None
        pass

    def next(self):
        pass

    def sound(self):
        pass

    def run(self):
        self._input.listen()

    def listen(self, event: GameEvent):
        print(event.description)
