from Worker import Worker


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        pass

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
