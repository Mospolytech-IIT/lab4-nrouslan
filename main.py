"""Модуль, являющийся точкой входа в программу для тестирования функций."""

from funcs.divide import divide
from funcs.get_name_by_id import get_name_by_id
from funcs.calculate_discount import calculate_discount
from funcs.copy_file import copy_file
from funcs.get_element_from_list import get_element_from_list
from funcs.generate_password import generate_password
from funcs.slice import slice
from funcs.sort_within_range import sort_within_range
from funcs.read_age import read_age
from funcs.read_file import read_file
from classes.BankAccount import BankAccount
from exceptions.InsufficientFundsException import InsufficientFundsException
from exceptions.IncorrectInputException import IncorrectInputException
from exceptions.InvalidFileException import InvalidFileException

def main():
    """Последовательно вызывает все функции из ЛР"""
    # ЗАДАНИЕ 1.

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

    # ЗАДАНИЕ 2.

    print(f"Итоговая скидка: {calculate_discount(-50, 5)}")
    print(f"Итоговая скидка: {calculate_discount(50, -5)}")

    print("\n---\n")

    # ЗАДАНИЕ 3.

    copy_file("./files/inputt.txt", "./files/output.txt")

    print("\n---\n")

    # ЗАДАНИЕ 4.

    print(f"get_element_from_list([], 0): {get_element_from_list([], 0)}")
    print(f"get_element_from_list([1, 2, 3], -5): {get_element_from_list([1, 2, 3], -5)}")
    print(f"get_element_from_list('', 1): {get_element_from_list('', 1)}")
    print(f"get_element_from_list([1, 2, 3], True): {get_element_from_list([1, 2, 3], [])}")

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

    # ЗАДАНИЕ 5.

    print(f"generate_password(8): {generate_password(2)}")
    print(f"generate_password(8): {generate_password(8, False, False, '', False)}")
    print(f"generate_password(8): {generate_password(8, False, False, False, False)}")

    print("\n---\n")

    # ЗАДАНИЕ 6.

    try:
        account = BankAccount(1000)
        account.withdraw_money(1500)
    except InsufficientFundsException as e:
        print(f"Ошибка снятия денег с банковского счета: {e}")

    try:
        name = input("Введите ваше имя: ")
        if len(name) < 2:
            raise IncorrectInputException("Введенное имя слишком короткое.")
        print(f"Ваше имя: {name}")
    except IncorrectInputException as e:
        print(f"Ошибка ввода имени: {e}")

    try:
        read_file("./files/unknown.txt")
    except InvalidFileException as e:
        print(f"Ошибка, некорректный файл: {e}")

    print("\n---\n")

    # ЗАДАНИЕ 7.

    age = read_age(8, 100)
    print(f"Ваш возраст: {age}")

    # ЗАДАНИЕ 8: По сути, функции account.withdraw_money, read_file и read_age 
    # уже демонстрируют работу созданных пользовательских исключений

if __name__ == "__main__":
    # ЗАДАНИЕ 9: Последовательный вызов функций
    main()
