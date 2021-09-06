from abc import ABC, abstractmethod
from mlattel.blaseball.events import GameEvent


class Audio(ABC):
    enabled: bool = True

    def toggle(self):
        self.enabled = not self.enabled

    @abstractmethod
    def startup(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    @abstractmethod
    def handle(self, event: GameEvent):
        pass