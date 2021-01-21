def parse_date(string):
    result = {}
    values = string.split('-')
    for index in range(0, 3):
        parsed_value = int(values[index] or 0)
        if index == 0:
            result['day'] = parsed_value
        elif index == 1:
            result['month'] = parsed_value
        elif index == 2:
            result['year'] = parsed_value
    return result


date_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# не учитываем высокосный день
def validate_day(day, month):
    return 0 < day <= date_in_month[month - 1]


def validate_month(month):
    return 0 < month < len(date_in_month)


def validate_year(year):
    return 0 < year


class Date:
    def __init__(self, date_string=None):
        self.date_string = date_string

    @classmethod
    def parse_date(cls, date):
        return parse_date(date.date_string)

    @staticmethod
    def validate_date(date):
        parsed = parse_date(date.date_string)
        return validate_month(parsed['month']) and validate_day(parsed['day'], parsed['month']) and validate_year(
            parsed['year'])
