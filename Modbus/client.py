import json
from typing import Dict, Optional, Any
from serial import Serial, SerialException



class SerialPortManager:
    """
    Класс для управления последовательным портом.
    """

    def __init__(self, port: str, baudrate: int = 9600, timeout: int = 1):
        """
        Инициализация объекта SerialPortManager.

        Attributes:
            port (str): Порт для инициализации.
            baudrate (int): Скорость передачи данных.
            timeout (int): Таймаут для операций чтения.
        """
        try:
            self.ser = Serial(port, baudrate, timeout=timeout)
            self.buffer = b''
        except SerialException:
            exit()


    def receive_line(self) -> str:
        """
        Чтение строки из последовательного порта - от символа фигурной скобки до символа новой строки.

        Returns:
            str: Результат чтения.
        """
        while True:
            byte = self.ser.read(1)
            if byte == b'\n':
                line = self.buffer.decode()
                self.buffer = b''
                if line.startswith('{"1'):
                    return line
            elif byte:
                self.buffer += byte

    def receive_json_data(self) -> Optional[Dict[str, Any]]:
        """
        Преобразование данных из строки в JSON а затем в словарь.

        Returns:
            Dict or None: Словарь с данными, при успешной отработке JSON иначе None
        """
        received_data = self.receive_line()
        if received_data:
            try:
                data_dict = json.loads(received_data)
                return data_dict
            except json.JSONDecodeError:
                return None
        return None

    def close_serial(self) -> None:
        """
        Закрытие соединения с последовательным портом.
        """
        self.ser.close()
