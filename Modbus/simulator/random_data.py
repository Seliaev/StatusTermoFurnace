from typing import Dict, Optional, Any


class RandomData:
    """
    Класс симуляции случайных данных для тестирования вместо реального устройства.

    Атрибуты:
    - __data (dict): Словарь для хранения сгенерированных случайных данных.
    """
    __slots__ = ['__data']

    @staticmethod
    def __generation_data():
        """
        Генерирует случайные данные от электропечи.

        Возвращает:
        dict: Словарь, содержащий 'status_supply' (статус электропечи),
                                  'active_minute' (время прошедшее с начала программы закалки)
                                  'temp_inside' (температура внутри электропечи)
        """
        from random import randint
        return {
            'status_supply': randint(0, 1),
            'active_minute': randint(0, 1200),
            'temp_inside': randint(500, 1250)
        }

    def __init__(self):
        self.__data = {}
        for i in range(1, 5):
            self.__data[f'{i}'] = self.__generation_data()

    def __call__(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        return self.__data

