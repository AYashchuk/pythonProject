from Car import Car


class CarWithLimit(Car):
    def __init__(self, name, speed, color, is_police, limit=40, car_type=''):
        super().__init__(name=name, speed=speed, color=color, is_police=is_police, car_type=car_type)
        self.__limit = limit

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__limit:
            print(f'For {self._type} speed should be less than {self.__limit}')
