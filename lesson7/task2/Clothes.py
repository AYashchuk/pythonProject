from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, v=0, h=0, name=''):
        self.name = name
        self.v = v
        self.h = h

    @abstractmethod
    def _count_expenses(self):
        pass

    @property
    def expensive(self):
        return self._count_expenses()
