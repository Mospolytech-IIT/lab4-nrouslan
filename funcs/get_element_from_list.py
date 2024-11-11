"""Модуль с функцией для получения элемента из списка."""

# ЗАДАНИЕ 4.

def get_element_from_list(list_data, index):
    """
    Возвращает элемент из списка по указанному индексу.
 
    Args:
        list_data (list): Список данных.
        index (int): Индекс элемента.

    Returns: 
        Элемент списка.
        None: Если возникла ошибка.
    """

    try:
        if not isinstance(list_data, list):
            raise TypeError("list_data должен быть списком.")

        if len(list_data) <= 0:
            raise ValueError("Список list_data пуст.")

        if not isinstance(index, int):
            raise TypeError("index должен быть целым числом.")

        return list_data[index]

    except TypeError as e:
        print(f"Ошибка типа: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return None
    except IndexError as e:
        print(f"Ошибка индекса: {e}")
        return None
