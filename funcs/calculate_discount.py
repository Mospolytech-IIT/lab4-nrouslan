"""Модуль с функцией для рассчета скидки на цену."""

# ЗАДАНИЕ 2.

def calculate_discount(price, discount_percentage):
    """
    Рассчитывает скидку на цену.

    Args:
        price (float): Исходная цена товара.
        discount_percentage (float): Процент скидки.

    Returns:
        float: Скидка на цену.
    """

    try:
        if price < 0:
            raise ValueError(
                f"Некорректная цена товара price: {price}. " +
                "Цена не может быть отрицательной.")
        if discount_percentage < 0:
            raise ValueError(
                f"Некорректный процент скидки товара discount_percentage: {discount_percentage}. " + 
                "Процент не может быть отрицательным.")
    except Exception as e:
        print(e)
        return 0

    return price * discount_percentage / 100
