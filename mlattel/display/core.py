from abc import ABC, abstractmethod
from mlattel.blaseball.events import GameEvent


class Display(ABC):
    @abstractmethod
    def show_score(self, home_score, away_score):
        pass

    @abstractmethod
    def show_count(self, inning, top, balls, strikes, outs):
        pass

    @abstractmethod
    def update(self, event: GameEvent):
        pass

    def clear(self):
        pass