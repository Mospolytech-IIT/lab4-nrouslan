"""Модуль с функцией, читающей и выводящей содержимое файла в консоль."""

import os
from exceptions.InvalidFileException import InvalidFileException

def read_file(filename):
    """
    Читает файл и выводит его содержимое в консоль.
    
    Args:
        filename (str): Имя файла.
        
    Raises:
    	InvalidFileException: Если файла не существует или у него некорректный формат.
    """

    try:
        if os.path.isfile(filename):
            with open(filename, "r") as f_in:
                print(f_in.read())
        else:
            raise FileNotFoundError
    except FileNotFoundError as e:
        raise InvalidFileException(f"Файл '{filename}' не найден.") from e
