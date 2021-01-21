from OfficeEquipment import OfficeEquipment, equipment_types


class Fax(OfficeEquipment):
    def __init__(self, cost, name):
        super().__init__(equipment_type=equipment_types['fax'], cost=cost, name=name)

    def running(self):
        print(f"Fax with id={self.id}, name={self.name} is running")
