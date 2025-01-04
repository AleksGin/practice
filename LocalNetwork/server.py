from typing import List

from data import Data


class Server:
    id_counter = 0

    def __init__(self) -> None:
        Server.id_counter += 1
        self.ip: int = Server.id_counter
        self.buffer: List[Data] = []
        self.router = None

    def send_data(self, data: Data) -> None:
        if self.router is None:
            raise ConnectionError("Данный сервер не привязан к роутеру")
        self.router.buffer.append(data)

    def get_data(self) -> List[Data]:
        elements_from_buffer = self.buffer[:]
        self.buffer.clear()
        return elements_from_buffer

    def get_ip(self) -> int:
        return self.ip
    
