"""Модуль с функцией для копирования данных из файла"""

import os

def copy_file(data_file, output_file):
    """
    Копирует данные из data_file в output_file.

    Args:
        data_file (str): Путь к файлу с данными.
        output_file (str): Путь к файлу для записи результата.
        
    Returns:
        bool: Результат копирования данных.

    Raises:
        FileNotFoundError: Если файл data_file не найден.
    """

    try:
        if os.path.isfile(data_file):
            with open(data_file, 'r') as f_in, open(output_file, 'w') as f_out:
                print(f"Копирование данных из {data_file} в {output_file}")
                for line in f_in:
                    f_out.write(line)
                return True
        else:
            raise FileNotFoundError(f"Файл {data_file} не найден!")
    except Exception as e:
        print(e)
        return False
    finally:
        print("Закрытие файлов...")
        f_in.close()
        f_out.close()