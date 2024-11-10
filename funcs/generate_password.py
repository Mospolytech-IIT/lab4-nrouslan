"""Модуль с функцией для генерации пароля."""

import random
import string

# TODO: Обрабатывать еще один тип исключения, или взять под другое задание

def generate_password(
    length,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_special_chars=True
):
    """
    Генерирует случайный пароль.

    Args:
        length (int): Длина пароля.
        include_uppercase (bool): Включать ли прописные буквы.
        include_lowercase (bool): Включать ли строчные буквы.
        include_digits (bool): Включать ли цифры.
        include_special_chars (bool): Включать ли специальные символы.

    Returns:
        str: Сгенерированный пароль.
        None: Если возникла ошибка.
    """

    try:
        if length < 8:
            raise ValueError("Длина пароля должна быть не менее 8 символов.")

        if not isinstance(include_uppercase, bool) or \
            not isinstance(include_lowercase, bool) or \
            not isinstance(include_digits, bool) or \
            not isinstance(include_special_chars, bool):
            raise TypeError("Все опциональные параметры должны быть булевыми значениями.")

        if not include_uppercase and \
            not include_lowercase and \
            not include_digits and \
            not include_special_chars:
            raise ValueError("Необходимо выбрать хотя бы один тип символов для включения в пароль.")

        characters = []

        if include_uppercase:
            characters.extend(string.ascii_uppercase)
        if include_lowercase:
            characters.extend(string.ascii_lowercase)
        if include_digits:
            characters.extend(string.digits)
        if include_special_chars:
            characters.extend(string.punctuation)

        password = ''.join(random.sample(characters, length))
        return password
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return None
    except TypeError as e:
        print(f"Ошибка типа: {e}")
        return None
        