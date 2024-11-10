"""Модуль, являющийся точкой входа в программу для тестирования функций."""

from funcs.divide import divide
from funcs.get_name_by_id import get_name_by_id
from funcs.calculate_discount import calculate_discount
from funcs.copy_file import copy_file
from funcs.get_element_from_list import get_element_from_list
from funcs.generate_password import generate_password
from funcs.slice import slice
from funcs.sort_within_range import sort_within_range

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

    print("\n---\n")

    print(f"get_element_from_list([], 0): {get_element_from_list([], 0)}")
    print(f"get_element_from_list([1, 2, 3], -5): {get_element_from_list([1, 2, 3], -5)}")
    print(f"get_element_from_list('', 1): {get_element_from_list('', 1)}")
    print(f"get_element_from_list([1, 2, 3], True): {get_element_from_list([1, 2, 3], [])}")

    print("\n---\n")

    # TODO: Продемонстрировать еще один тип исключения, или взять под другое задание

    print(f"generate_password(8): {generate_password(2)}")
    print(f"generate_password(8): {generate_password(8, False, False, '', False)}")
    print(f"generate_password(8): {generate_password(8, False, False, False, False)}")

    print("\n---\n")

    print(f"slice(''): {slice('')}")
    print(f"slice([]): {slice([])}")
    print(f"slice([1, 2, 3], -1, 2): {slice([1, 2, 3], -1, 2)}")

    print("\n---\n")

    print(f"sort_within_range('', 3, 7): {sort_within_range('', 3, 7)}")
    print(f"sort_within_range([], 3, 7): {sort_within_range([], 3, 7)}")
    print("sort_within_range([5, 1, 8, 3, 6, 2, 9, 4, 7], -3, -7): " +
          f"{sort_within_range([5, 1, 8, 3, 6, 2, 9, 4, 7], -3, -7)}")

    print("\n---\n")
