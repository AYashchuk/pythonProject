from Car import Car
from CarTypes import CarTypes


class SportCar(Car):
    def __init__(self):
        super().__init__(name="SportCar", speed=0, color='red', is_police=False, car_type=CarTypes.SportCar)
