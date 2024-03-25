import io
import logging
from contextlib import contextmanager, redirect_stdout
from json import dumps
from multiprocessing import Process
from time import sleep

from flask import Flask

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class Server:
    def __init__(self, host, port, data):
        self.__host__ = host
        self.__port__ = port
        self.__data__ = data

    @contextmanager
    def run(self):
        p = Process(target=self.server)
        p.start()
        sleep(1)
        yield
        p.kill()

    def server(self):
        _ = io.StringIO()
        with redirect_stdout(_):
            app = Flask(__name__)

            @app.route('/')
            def index():
                return dumps(self.__data__)

            app.run(self.__host__, self.__port__)


if __name__ == '__main__':
    data = {
        "2023/04/01": [
            {"galaxy": "M30", "type": "bar", "brightness": 9},
            {"galaxy": "M31", "type": "bar", "brightness": 11}
        ],
        "2023/04/03": [
            {"galaxy": "M30", "type": "bar", "brightness": 5},
            {"galaxy": "M16", "type": "wrong", "brightness": -3},
            {"galaxy": "M30", "type": "bar", "brightness": 7}
        ],
        "2023/01/01": [
            {"galaxy": "M29", "type": "elliptical", "brightness": 12},
            {"galaxy": "M30", "type": "bar", "brightness": 8}
        ]
    }

    server = Server('127.0.0.1', 5000, data)
    with server.run():
        while (row := input('Введите "stop" для завершения работы сервера: ')) != 'stop':
            ...
