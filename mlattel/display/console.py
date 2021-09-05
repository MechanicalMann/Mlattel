from mlattel.blaseball.events import GameEvent
from mlattel.display.core import Display

ORDINALS = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']


class ConsoleDisplay(Display):
    def show_count(self, inning, top, balls, strikes, outs):
        print(
            f'{"Top" if top else "Bottom"} of {inning}, {balls}-{strikes}, {outs} out'
        )

    def show_score(self, home_score, away_score):
        print(f'Away: {away_score}, Home: {home_score}')

    def update(self, event: GameEvent):
        if (event.description):
            self.show_count(event.inning, event.top, event.balls,
                            event.strikes, event.outs)
            if len(event.runners) > 0:
                runners = ', '.join(
                    [ORDINALS[b] for b in event.bases_occupied])
                print(f'Runners on {runners}')
            print(event.description)
