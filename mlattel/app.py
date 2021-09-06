import asyncio
from mlattel.audio import Audio
from threading import Thread
from mlattel.display.core import Display
from mlattel.blaseball.events import EventListener, Game, GameEvent
from mlattel.input import Input


class App(EventListener):
    def __init__(self, input: Input, display: Display, audio: Audio) -> None:
        self.game = None
        self._audio = audio
        self._display = display
        self._input_loop = None
        self._game_loop = None
        self._task = None
        self._thread = None
        self._input = input
        self._input.on_press_start = self.start
        self._input.on_press_next = self.next
        self._input.on_press_sound = self.sound
        self._input.on_press_score = self.show_score
        self._input.on_release_score = self.hide_score

    def show_score(self, *args):
        if not self.game:
            print('No active game')
        self._display.show_score(self.game.home_score, self.game.away_score)

    def hide_score(self, *args):
        self._display.show_count(self.game.inning, self.game.top,
                                 self.game.balls, self.game.strikes,
                                 self.game.outs)

    def start(self, *args):
        if not self.game:
            print('Starting...')
            self.game = Game('1bf2ec1a-4df8-4446-b7f0-55ba901d4f30', self)
            self._game_loop = asyncio.new_event_loop()
            self._task = self._game_loop.create_task(self.game.get_events())
            self._thread = Thread(target=self._game_loop.run_forever)
            try:
                self._thread.start()
                self._audio.startup()
            except Exception:
                print('Failure!')
        else:
            print('Stopping...')
            self.stop()
        pass

    def next(self, *args):
        pass

    def sound(self, *args):
        self._audio.toggle()

    def run(self):
        self._input.listen()

    def stop(self):
        if not self.game:
            return
        self._display.clear()
        self._game_loop.call_soon_threadsafe(self._game_loop.stop)
        self._task.cancel()
        self._thread.join()
        self._audio.shutdown()
        self.game = None
        self._game_loop = None
        self._thread = None

    def listen(self, event: GameEvent):
        self._display.update(event)
        self._audio.handle(event)
