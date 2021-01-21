from OfficeEquipment import OfficeEquipment, equipment_types


class Scanner(OfficeEquipment):
    def __init__(self, cost, name):
        super().__init__(equipment_type=equipment_types['scanner'], cost=cost, name=name)

    def running(self):
        print(f"Scanner with id={self.id}, name={self.name} is running")
