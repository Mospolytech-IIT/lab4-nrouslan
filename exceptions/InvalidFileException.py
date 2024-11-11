"""Модуль с исключением, возникающим при попытке обработать неверный файл."""

class InvalidFileException(Exception):
    """Исключение, возникающее при попытке обработать неверный файл."""
    def __init__(self, message):
        super().__init__(message)
