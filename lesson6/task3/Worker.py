default_income = {"wage": 0, "bonus": 0}


class Worker:
    def __init__(self, name, surname, position, income=None):
        self.name = name
        self.surname = surname
        self.position = position
        if income is None:
            self._income = default_income
        else:
            self._income = income

    def set_income(self, income):
        self._income = income
