import logging
import uvicorn

from management.base import BaseCommand

class Command(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        
    def execute(self, *args, **options):
        # выполнять код тут
        try:
            host, port = "0.0.0.0", 8000
            logging.info('Meow ^_^')
            logging.info(f'run_web_server host: http://{host}:{port}')
            uvicorn.run("api.asgi:app", host=host, port=port, reload=True)  # Передача приложения как строки импорта
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        
        # return super().execute(*args, **options)
    
    def handle(self, *args, **options):
        # перехватывать ошибки и состояния тут
        ...