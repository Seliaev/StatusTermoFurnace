from Modbus.client import SerialPortManager
from typing import Dict


def get_data_from_sp(port: str='/dev/ttyACM0', test: bool=False) -> Dict | None:
    """
    Получает данные из SerialPortManager в формате JSON.

    Attributes:
        port (str): Порт от устройства для инициализации SerialPortManager. По умолчанию '/dev/ttyACM0'.
        test (bool): Запуск симуляции, при отключенном устройстве (рандомные данные). По умолчанию False.


    Returns:
        dict or None: Словари с данными или None, если данные не были получены.

        {
            "1": {
            "status_supply": 1,
            "active_minute": 123,
            "temp_inside": 1000
          },
            "2": {
            "status_supply": 0,
            "active_minute": 456,
            "temp_inside": 800
          },
            "3": {
            "status_supply": 1,
            "active_minute": 789,
            "temp_inside": 1200
          },
            "4": {
            "status_supply": 0,
            "active_minute": 1011,
            "temp_inside": 900
          }
        }
    """
    if not test:
        serial_manager = SerialPortManager(port=port, baudrate=9600)
        try:
            received_data = serial_manager.receive_json_data()
            if received_data:
                return received_data
            else:
                return None
        finally:
            serial_manager.close_serial()
    else:
        from Modbus.simulator.random_data import RandomData
        received_data = RandomData()
        return received_data.__call__()

