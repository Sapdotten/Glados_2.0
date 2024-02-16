import logging
import sys
from utils.config_manager import Logger


def start():
    print('Запуск логгера')
    # формат вывода логов
    log_format = '%(asctime)s - %(levelname)s - %(message)s - %(args)s'

    is_console = Logger.is_console()
    if is_console == 0:
        file_handler = logging.FileHandler(Logger.file())
        file_handler.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.ERROR)
        handlers = [file_handler, stream_handler]
    elif is_console == 1:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO)
        handlers = [stream_handler]
    else:
        raise ValueError('Unexpected value for log out')

    logging.basicConfig(
        handlers=handlers,
        level=Logger.level(),
        format=log_format
    )
