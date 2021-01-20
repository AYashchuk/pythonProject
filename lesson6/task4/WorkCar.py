from CarWithLimit import CarWithLimit
from CarTypes import CarTypes


class WorkCar(CarWithLimit):
    def __init__(self):
        super().__init__(name="WorkCar", speed=0, color='red', is_police=False, limit=40, car_type=CarTypes.WorkCar)
