from OfficeEquipment import OfficeEquipment, equipment_types


class Printer(OfficeEquipment):
    def __init__(self, cost, name):
        super().__init__(equipment_type=equipment_types['printer'], cost=cost, name=name)

    def running(self):
        print(f"Printer with id={self.id}, name={self.name} is running")
