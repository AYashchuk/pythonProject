from abc import ABC, abstractmethod
from random import randrange

equipment_types = {
    'fax': 'fax',
    'printer': 'printer',
    'scanner': 'scanner'
}


class OfficeEquipment(ABC):
    def __init__(self, equipment_type, cost, name):
        # simple unique id generation
        self._id = randrange(0, 1000000)
        self._type = equipment_type
        self._cost = cost
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def cost(self):
        return self._cost

    @property
    def name(self):
        return self._name

    @abstractmethod
    def running(self):
        pass

    def __str__(self):
        return f"{self._name}/{self._id}/{self._type}"

