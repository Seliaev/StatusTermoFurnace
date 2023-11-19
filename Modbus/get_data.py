from Modbus.client import SerialPortManager
from typing import Dict


def get_data_from_sp(port: str = '/dev/ttyACM0') -> Dict | None:
    """
    Получает данные из SerialPortManager в формате JSON.

    Attributes:
        port (str): Порт от устройства для инициализации SerialPortManager. По умолчанию '/dev/ttyACM0'.

    Returns:
        dict or None: Словарь с данными или None, если данные не были получены.
        {'channel_furnace': 1, 'status_supply': 0, 'active_minute': 30, 'temp_inside': 750}
    """
    serial_manager = SerialPortManager(port=port, baudrate=9600)
    try:
        received_data = serial_manager.receive_json_data()
        if received_data:
            return received_data
        else:
            return None
    finally:
        serial_manager.close_serial()

