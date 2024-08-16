import sys, os
import logging
import colorlog
from utils.config_manager import LoggerConfigs

def start():
    log_format = colorlog.ColoredFormatter(
        '[%(asctime)s] %(log_color)s%(levelname)s:%(reset)s %(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger()
    logger.setLevel(LoggerConfigs.level())

    is_console = LoggerConfigs.is_console()
    handlers = []

    if is_console == 0:
        try:
            file_handler = logging.FileHandler(LoggerConfigs.file())
        except FileNotFoundError as e:
            log_file_path = LoggerConfigs.file()
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            with open(log_file_path, 'a'):
                os.utime(log_file_path, None)
            logging.warning(f"{e}\nФайл логов был создан!")
            file_handler = logging.FileHandler(log_file_path)
        
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(log_format)
        handlers.append(file_handler)

    if is_console in [0, 1]:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.INFO if is_console == 1 else logging.ERROR)
        stream_handler.setFormatter(log_format)
        handlers.append(stream_handler)

    if not handlers:
        raise ValueError('Unexpected value for log out')

    for handler in handlers:
        logger.addHandler(handler)