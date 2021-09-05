import asyncio
from mlattel.display.core import Display
from mlattel.blaseball.events import EventListener, Game, GameEvent
from mlattel.input import Input


class App(EventListener):
    def __init__(self, input: Input, display: Display) -> None:
        self.game = None
        self._display = display
        self._input_loop = None
        self._game_loop = None
        self._input = input
        self._input.on_press_start = self.start
        self._input.on_press_next = self.next
        self._input.on_press_sound = self.sound
        self._input.on_press_score = self.show_score
        self._input.on_release_score = self.hide_score

    def show_score(self):
        if not self.game:
            print('No active game')
        self._display.show_score(self.game.home_score, self.game.away_score)

    def hide_score(self):
        self._display.show_count(self.game.inning, self.game.top,
                                 self.game.balls, self.game.strikes,
                                 self.game.outs)

    def start(self):
        if not self.game:
            self.game = Game('53c3e12c-5a94-49ea-9804-4358aee1edb6', self)
            self._game_loop = asyncio.new_event_loop()
            try:
                self._game_loop.run_until_complete(self.game.get_events())
            except KeyboardInterrupt:
                self._game_loop.close()
                self.game = None
            except Exception:
                print('Failure!')
        else:
            self._game_loop.close()
            self.game = None
        pass

    def next(self):
        pass

    def sound(self):
        pass

    def run(self):
        self._input_loop = asyncio.new_event_loop()
        try:
            self._input_loop.run_until_complete(self._input.listen())
        except KeyboardInterrupt:
            self._input_loop.close()

    def listen(self, event: GameEvent):
        self._display.update(event)
