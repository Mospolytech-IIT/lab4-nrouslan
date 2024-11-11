"""Модуль с классом банковского счета."""

from exceptions.InsufficientFundsException import InsufficientFundsException

# ЗАДАНИЯ 6 И 8.

class BankAccount:
    """Класс банковского счета."""

    def __init__(self, balance):
        self.balance = balance

    def withdraw_money(self, count):
        """
        Снимает деньги со счета.
        
        Args:
            count (float): Количество денег.
        
        Raises:
            InsufficientFundsException: Когда на счету недостаточно средств.
        """

        if count > self.balance:
            raise InsufficientFundsException("Недостаточно средств на счету.")

        self.balance -= count

        print(f"Снято {count} рублей. Остаток: {self.balance}")
