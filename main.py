"""Модуль, являющийся точкой входа в программу для тестирования функций."""

from funcs.divide import divide
from funcs.get_name_by_id import get_name_by_id
from funcs.calculate_discount import calculate_discount
from funcs.copy_file import copy_file

if __name__ == "__main__":
    try:
        print(divide(1, 0))
    except ZeroDivisionError as e:
        print(f"При делении числа возникла ошибка: {e}")

    print("\n---\n")

    try:
        print(get_name_by_id(-5))
    except ValueError as e:
        print(e)

    print("\n---\n")

    print(f"Итоговая скидка: {calculate_discount(-50, 5)}")
    print(f"Итоговая скидка: {calculate_discount(50, -5)}")

    print("\n---\n")

    copy_file("./files/input.txt", "./files/output.txt")
