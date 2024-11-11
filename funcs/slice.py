"""Модуль с функцией для создания срезов массива по индексам."""

# ЗАДАНИЕ 4.

def slice(list_data, start=None, stop=None, step=None):
    """
    Осуществляет срез массива по индексам.
    
    Args:
        list_data (list): Исходный массив.
        start (int): Начальный индекс (включительно).
        stop (int): Конечный индекс (не включительно).
        step (int): Шаг среза.

    Returns:
        list: Новый объект с данными, полученными из среза.
    """

    try:
        if not isinstance(list_data, list):
            raise TypeError("list_data должен быть списком.")

        if len(list_data) <= 0:
            raise ValueError("Список list_data пуст.")

        if not isinstance(start, int) and not start is None:
            raise TypeError("start должен быть целым числом или None.")

        if not isinstance(stop, int) and not stop is None:
            raise TypeError("start должен быть целым числом или None.")

        if not isinstance(step, int) and not step is None:
            raise TypeError("step должен быть целым числом или None.")

        if start is None:
            start = 0
        if stop is None:
            stop = len(list_data)
        if step is None:
            step = 1

        if start < 0 or start > len(list_data):
            raise IndexError(f"Значение start = {start} выходит за границы массива.")

        if stop < 0 or stop > len(list_data):
            raise IndexError(f"Значение stop = {stop} выходит за границы массива.")

        result = []

        for i in range(start, stop, step):
            if 0 <= i < len(list_data):
                result.append(list_data[i])

        return result
    except TypeError as e:
        print(f"Ошибка типа: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return None
    except IndexError as e:
        print(f"Ошибка индекса: {e}")
        return None
