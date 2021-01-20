from CarWithLimit import CarWithLimit
from CarTypes import CarTypes


class TownCar(CarWithLimit):
    def __init__(self):
        super().__init__(name="TownCar", speed=0, color='red', is_police=False, limit=60, car_type=CarTypes.TownCar)

