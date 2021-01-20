# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--hours")
parser.add_argument("--rate")
parser.add_argument("--bonus")
args = parser.parse_args()


def wage(hours, rate, bonus):
    return (hours * rate) + bonus


print(wage(hours=int(args.hours), rate=int(args.rate), bonus=int(args.bonus)))
