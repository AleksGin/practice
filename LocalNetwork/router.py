from typing import List

from data import Data
from server import Server


class Router:
    def __init__(self) -> None:
        self.buffer: List[Data] = []
        self.servers: dict[int, Server] = {}

    def link(self, server: Server) -> None:
        if server.get_ip() in self.servers:
            raise ValueError(f"Сервер с IP: {server.get_ip()} уже привязан к роутеру")
        server.router = self
        self.servers[server.get_ip()] = server

    def unlink(self, server: Server) -> None:
        if server.get_ip() not in self.servers:
            raise KeyError(f"Сервер с IP: {server.get_ip()} не привязан к роутеру")
        del self.servers[server.get_ip()]
        server.router = None

    def send_data(self) -> None:
        for packet in self.buffer:
            destination_server = self.servers.get(packet.server_number)
            if destination_server is None:
                raise ValueError(
                    f"Сервер с IP: {packet.server_number} не привязан к роутеру"
                )
            destination_server.buffer.append(packet)
        self.buffer.clear()
