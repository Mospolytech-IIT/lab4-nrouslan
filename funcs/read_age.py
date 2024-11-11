"""Модуль с функцией, читающей ввод возраста пользователя с клавиатуры."""

from exceptions.IncorrectInputException import IncorrectInputException

# ЗАДАНИЯ 7 И 8.

def read_age(minAge, maxAge):
    """
    Читает ввод возраста пользователя с клавиатуры.
    
    Args:
        minAge (int): Минимальный возраст.
        maxAge (int): Максимальный возраст.

    Returns:
        int: Возраст пользователя.
    """

    age = input("Введите ваш возраст: ")

    try:
        try:
            age = int(age)
            if age < minAge or age > maxAge:
                raise IncorrectInputException(
                    f"Возраст должен быть в диапазоне от {minAge} до {maxAge}.")
            else:
                return age
        except ValueError as e:
            raise IncorrectInputException("Введенное значение не является числом.") from e
    except IncorrectInputException as e:
        print(f"Ошибка ввода возраста: {e}")
        return read_age(minAge, maxAge)
