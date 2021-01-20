class Car:
    def __init__(self, name, speed=0, color='red', is_police=False, car_type=''):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self._type = car_type

    def go(self):
        if self.speed == 0:
            print(f'Car {self.name} is staying, please set speed')
        else:
            print(f'Car {self.name} is going, speed {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Car {self.name} had stopped')

    def turn(self, direction):
        print(f'Car {self.name} turn into f{direction}')

    def show_speed(self):
        print(f'Car {self.name} has current speed {self.speed}')

    def __str__(self):
        return f"Car {self.name}, speed: {self.speed}, color: {self.color}, {self.is_police}"
