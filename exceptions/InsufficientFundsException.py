"""Модуль с исключением, возникающим при недостатке средств."""

class InsufficientFundsException(Exception):
    """Исключение, возникающее при недостатке средств."""
    def __init__(self, message):
        super().__init__(message)
