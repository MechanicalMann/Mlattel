from abc import ABC, abstractmethod
import asyncio
from blaseball_mike import database as datablase, eventually, chronicler
from mlattel.blaseball.types import EventType, guess_event_type


# Surely there's a way we could... not do this
class GameEvent(object):
    def __init__(self, event: dict, **kwargs) -> None:
        self.id = event['id']
        self.type = None
        self.balls = event['atBatBalls']
        self.strikes = event['atBatStrikes']
        self.outs = event['halfInningOuts']
        self.inning = event['inning'] + 1
        self.inning_runs = event['halfInningScore']
        self.top = event['topOfInning']
        self.game_started = event['gameStart']
        self.game_over = event['gameComplete']
        self.away_score = event['awayScore']
        self.home_score = event['homeScore']
        self.away_pitcher = event['awayPitcherName']
        self.home_pitcher = event['homePitcherName']
        self.runners = event['baseRunnerNames']
        self.bases_occupied = event['basesOccupied']
        if event['awayBatterName']:
            self.batter = event['awayBatterName']
        else:
            self.batter = event['homeBatterName']
        self.description = None
        if 'lastUpdate' in event and event['lastUpdate']:
            self.description = event['lastUpdate']
            self.type = guess_event_type(self.description)
        if self.home_pitcher and not self.description:
            # Sometimes instead of "let's go" we get a blank update with the
            # pitchers set.  We'll consider them equivalent for convenience
            self.type = EventType.LETS_GO
        for k in kwargs:
            self.__setattr__(k, kwargs[k])


class EventListener(ABC):
    @abstractmethod
    def listen(self, event: GameEvent):
        pass


class Game(object):
    def __init__(self, game_id: str, listener: EventListener) -> None:
        self.id = game_id
        self.listener = listener
        game = datablase.get_game_by_id(game_id)
        if not game:
            raise ValueError('Invalid game ID')
        self.season = game['season'] + 1
        self.day = game['day'] + 1
        self.home_team = game['homeTeamName']
        self.home_team_nick = game['homeTeamNickname']
        self.away_team = game['awayTeamName']
        self.away_team_nick = game['awayTeamNickname']
        self.home_pitcher = game['homePitcherName']
        self.away_pitcher = game['awayPitcherName']
        self.runners = []
        self.bases_occupied = []
        self.home_score = 0
        self.away_score = 0
        self.inning = 0
        self.top = True
        self.balls = 0
        self.strikes = 0
        self.outs = 0
        if 'weather' in game and game['weather']:
            self.weather_id = int(game['weather'])
            weather = datablase.get_weather()
            self.weather = weather[self.weather_id]['name']
        if 'stadium' in game and game['stadium']:
            self.stadium_id = game['stadium']
            # There ... might be no way to get the stadium name from the API
        self.prev = None

    async def get_events(self):
        for event in chronicler.get_game_updates(
                game_ids=['1bf2ec1a-4df8-4446-b7f0-55ba901d4f30'], lazy=True):
            if not 'data' in event:
                continue
            ge = GameEvent(event['data'], game=self)
            self.home_score = ge.home_score
            self.away_score = ge.away_score
            self.inning = ge.inning
            self.top = ge.top
            self.balls = ge.balls
            self.strikes = ge.strikes
            self.outs = ge.outs
            self.runners = ge.runners
            self.bases_occupied = ge.bases_occupied
            self.listener.listen(ge)
            self.prev = ge
            await asyncio.sleep(4)  # roughly approximate a real game feed