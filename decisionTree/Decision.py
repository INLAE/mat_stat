from abc import ABC, abstractmethod

from IEntity import IEntity


class Decision(ABC):
    @abstractmethod
    def evaluate(self, entity: IEntity):
        pass
