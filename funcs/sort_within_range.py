"""Модуль для сортировки значений в массиве arr в пределах диапазона"""

def sort_within_range(arr, start, end):
    """
    Сортирует значения в массиве arr в пределах диапазона [start, end].

    Args:
        arr (list): Массив, который нужно отсортировать.
        start (int): Начальное значение диапазона.
        end (int): Конечное значение диапазона.

    Returns:
        list: Отсортированный массив, содержащий только значения в заданном диапазоне.
    """

    try:
        if not isinstance(arr, list):
            raise TypeError("arr должен быть списком.")

        if len(arr) <= 0:
            raise ValueError("Список arr пуст.")

        if not isinstance(start, int):
            raise TypeError("start должен быть целым числом.")

        if not isinstance(end, int):
            raise TypeError("end должен быть целым числом.")

        if start < 0 or start > len(arr):
            raise IndexError(f"Значение start = {start} выходит за границы массива.")

        if end < 0 or end > len(arr):
            raise IndexError(f"Значение end = {end} выходит за границы массива.")


        # Фильтруем значения в заданном диапазоне.
        filtered_arr = [x for x in arr if start <= x <= end]

        # Сортируем отфильтрованный массив.
        filtered_arr.sort()

        return filtered_arr
    except TypeError as e:
        print(f"Ошибка типа: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return None
    except IndexError as e:
        print(f"Ошибка индекса: {e}")
        return None
