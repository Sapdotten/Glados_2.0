import logging, asyncio
from core.management.base import BaseCommand

from utils.db_operations import create_tables


logger = logging.getLogger(__name__)



class Command(BaseCommand):
    help = 'Создание всех таблиц в базе данных с использованием SQLAlchemy'

    def handle(self, *args, **options):
        try:
            # Запуск асинхронного кода в отдельном потоке
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(create_tables())
            loop.close()
            logger.info('Таблицы успешно созданы')
        except Exception as e:
            logger.error(f'Ошибка при создании таблиц: {e}')