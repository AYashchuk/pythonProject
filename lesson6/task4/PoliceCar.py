from Car import Car
from CarTypes import CarTypes


class PoliceCar(Car):
    def __init__(self):
        super().__init__(name="PoliceCar", speed=0, color='red', is_police=True, car_type=CarTypes.PoliceCar)
