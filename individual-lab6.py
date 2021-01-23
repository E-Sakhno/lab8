#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 5. Использовать словарь, содержащий следующие ключи:
# название пункта назначения рейса;
# номер рейса;
# тип самолета.

# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены в алфавитном порядке по названиям пунктов назначения;
# вывод на экран пунктов назначения и номеров рейсов, обслуживаемых самолетом, тип которого введен с клавиатуры;
# если таких рейсов нет, выдать на дисплей соответствующее сообщение.

import sys


def add(flights):
    # Запросить данные о рейсах.
    destination = input("Пункт назначения? ")
    numb = input("Номер рейса? ")
    fl_type = input("Тип самолета? ")
    # Создать словарь.
    flight = {
        'destination': destination,
        'numb': numb,
        'fl_type': fl_type,
    }
    # Добавить словарь в список.
    flights.append(flight)
    # Отсортировать список в случае необходимости.
    if len(flights) > 1:
        flights.sort(key=lambda item: item.get('destination', ''))


def show_list(flights):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 16
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^16} |'.format(
            "№",
            "Пункт назначения",
            "Номер рейса",
            "Тип самолета"
        )
    )
    print(line)
    # Вывести данные о всех рейсах.
    for idx, flight in enumerate(flights, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>16} |'.format(
                idx,
                flight.get('destination', ''),
                flight.get('numb', ''),
                flight.get('fl_type', 0)
            )
        )
        print(line)


def select(flights):
    parts = command.split(' ', maxsplit=1)
    # Инициализировать счетчик.
    count = 0
    # Проверить сведения о рейсах из списка.
    for flight in flights:
        if flight.get('fl_type') == parts[1]:
            count += 1
            print(
                '{:>4}: {}'.format(count, flight.get('destination', ''))
            )
    # Если счетчик равен 0, то работники не найдены.
    if count == 0:
        print("Рейсы с заданным типом самолета не найдены")


def help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рейсов;")
    print("select <тип> - запросить рейсы с определенным типом самолета;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    # Список полётов.
    flights = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            add(flights)
        elif command == 'list':
            show_list(flights)
        elif command.startswith('select '):
            select(flights)
        elif command == 'help':
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
