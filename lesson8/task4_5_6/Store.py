from functools import reduce

from lesson8.task4_5_6.NotOfficeEquipmentError import NotOfficeEquipmentError
from lesson8.task4_5_6.OfficeEquipment import equipment_types, OfficeEquipment


def to_string(target_list):
    index = 0
    while index < len(target_list):
        yield f"{target_list[index]}"
        index += 1


def get_costs_array(target_list):
    index = 0
    while index < len(target_list):
        yield target_list[index].cost
        index += 1


class Store:
    def __init__(self):
        self.__items = []

    def add(self, item):
        # why method isinstance return false ???
        # if not isinstance(item, OfficeEquipment):
        #     raise NotOfficeEquipmentError(f'Added value {item} isn`t office equipment')
        self.__items.append(item)

    def del_item(self, target):
        for index, item in enumerate(self.__items):
            if item.id == target.id:
                del self.__items[index]
                return

    def __str__(self):
        return f"{[el for el in to_string(self.__items)]}"

    def get_total_cost(self):
        costs = [el for el in get_costs_array(self.__items)]
        return reduce(lambda el_prev, el: el + el_prev, costs)

    def run_all(self):
        for item in self.__items:
            item.running()

    def get_stats(self):
        result = {}
        for key in equipment_types:
            result[key] = 0

        for item in self.__items:
            result[item.type] += 1

        return result
