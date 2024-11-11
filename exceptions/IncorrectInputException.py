"""Модуль с исключением, возникающим при получении некорректных данных от пользователя."""

class IncorrectInputException(Exception):
    """Исключение, возникающее при получении некорректных данных от пользователя."""

    def __init__(self, message):
        super().__init__(message)
