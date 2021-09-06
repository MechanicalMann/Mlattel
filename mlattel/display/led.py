from time import sleep
from PIL.ImageDraw import ImageDraw
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import sevensegment
from luma.led_matrix.device import max7219
from mlattel.blaseball.events import GameEvent
from mlattel.blaseball.types import EventType
from mlattel.display.core import Display

BASES = [(2, 8), (8, 8), (8, 2), (13, 2), (13, 13), (2, 13)]
PITCHES = [
    EventType.BALL,
    EventType.STRIKE,
    EventType.WALK,
    EventType.STRIKEOUT,
    EventType.HIT_BY_PITCH,
    EventType.HIT,
    EventType.FOUL,
    EventType.HOME_RUN,
    EventType.FLYOUT,
    EventType.GROUNDOUT,
]


class LedDisplay(Display):
    def __init__(self) -> None:
        digit_serial = spi(port=0, device=0, gpio=noop())
        digit_device = max7219(digit_serial)

        matrix_serial = spi(port=1, device=0, gpio=noop())
        self._matrix = max7219(matrix_serial,
                               width=16,
                               height=16,
                               block_orientation=-90)
        self._digits = sevensegment(digit_device)
        self._matrix.contrast(95)
        self._digits.device.contrast(255)

    def show_count(self, inning, top, balls, strikes, outs):
        text = f'{inning: 2}{"" if top else "."}{outs: 2}{balls: 2}{strikes: 2}'
        print(text)
        self._digits.text = text

    def show_score(self, home_score, away_score):
        h = home_score if isinstance(home_score, int) else f'{home_score:.1f}'
        a = away_score if isinstance(away_score, int) else f'{away_score:.1f}'
        text = f'{a: 4}{h: 4}'
        print(text)
        self._digits.text = text

    def clear(self):
        self._digits.text = ''
        with canvas(self._matrix) as draw:
            self.clear_field(draw)

    def clear_field(self, draw: ImageDraw):
        draw.rectangle([(0, 0), (15, 15)], fill='black')

    def _draw_state(self, event: GameEvent, draw: ImageDraw):
        self.clear_field(draw)

        if not event:
            return

        # Populate baserunners
        for base in event.bases_occupied:
            if base >= len(BASES):
                continue
            draw.point(BASES[base], fill='white')

    def update(self, event: GameEvent):
        # Animate pitch
        if event.type in PITCHES:
            for frame in [(6, 6), (5, 5), (4, 4), (3, 3)]:
                with canvas(self._matrix) as draw:
                    self._draw_state(event.prev, draw)
                    draw.point(frame, fill='white')
                    sleep(0.1)

        if event.type == None and not event.game_started:
            self._digits.text = f'{event.game.away_team_nick[0:4].upper()}{event.game.home_team_nick[0:4].upper()}'
        if event.type == EventType.LETS_GO:
            pitching = f'{event.game.away_pitcher.upper()} vs {event.game.home_pitcher.upper()}'
            self._digits.text = pitching[0:8]
            sleep(0.5)
            for offset in range(1, len(pitching) - 7):
                self._digits.text = pitching[offset:offset + 8]
                sleep(0.1)
        elif event.type == EventType.PLAY_BALL:
            self._digits.text = 'PLAYBALL'
        elif event.game_over or event.type == EventType.GAME_OVER or event.type == EventType.GAME_ENDED or event.type == EventType.GAME_CANCELED or event.type == EventType.GAME_END_LOG:
            self.show_score(event.home_score, event.away_score)
        elif event.type == EventType.END_OF_INNING:
            self.show_score(event.home_score, event.away_score)
        elif event.type == EventType.INNING_CHANGE:
            team = (event.game.away_team_nick
                    if event.top else event.game.home_team_nick).upper()
            self._digits.text = team[0:8]
            if len(team) > 8:
                sleep(0.5)
                for offset in range(1, len(team) - 7):
                    self._digits.text = team[offset:offset + 8]
                    sleep(0.1)
        elif event.type == EventType.NOW_BATTING:
            batter = event.batter.upper()
            self._digits.text = batter[0:8]
            if len(batter) > 8:
                sleep(0.5)
                for offset in range(1, len(batter) - 7):
                    self._digits.text = batter[offset:offset + 8]
                    sleep(0.1)
        elif event.prev and (event.home_score != event.prev.home_score
                             or event.away_score != event.prev.away_score):
            self.show_score(event.home_score, event.away_score)
        else:
            self.show_count(event.inning, event.top, event.balls,
                            event.strikes, event.outs)
        print(event.description)

        with canvas(self._matrix) as draw:
            self._draw_state(event, draw)

            # Handle common outcomes
            if event.type == EventType.BALL or event.type == EventType.WALK or event.type == EventType.MILD_PITCH:
                draw.point((1, 2), fill='white')
            if event.type == EventType.HIT_BY_PITCH:
                draw.point((2, 1), fill='white')
            elif event.type == EventType.STRIKE or event.type == EventType.STRIKEOUT:
                draw.point((1, 1), fill='white')
            elif event.type == EventType.FOUL:
                draw.point((0, 6), fill='white')
            elif event.type == EventType.HIT:
                draw.point((2, 2), fill='white')
                draw.point((4, 10), fill='white')
            elif event.type == EventType.HOME_RUN:
                draw.point((2, 2), fill='white')
                draw.point((15, 15), fill='white')
            elif event.type == EventType.GROUNDOUT:
                draw.point((2, 2), fill='white')
                draw.point((9, 6), fill='white')
            elif event.type == EventType.FLYOUT:
                draw.point((2, 2), fill='white')
                draw.point((12, 12), fill='white')
