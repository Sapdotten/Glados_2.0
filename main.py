import logging
import sys
import signal
from core.management.utils import (
    execute_from_command_line,
    execute_from_input_stream
)

def signal_handler(sig, frame):
    # перехватывает ctrl+c
    logging.info("Exiting the program.")
    sys.exit(0)

if __name__ == '__main__':
    # запуск логера
    from utils.logger import start as init_logger
    init_logger()
    
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    logging.info('Logger is launched')
    
    # перехват сигнала SIGINT
    signal.signal(signal.SIGINT, signal_handler)

    execute_from_command_line()
    
    try:
        while True:
            command = input("--> ")
            execute_from_input_stream(command)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)