# core/management/commands/revision.py
from core.management.base import BaseCommand
from subprocess import call
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Run Alembic autogenerate'

    def add_arguments(self, parser):
        parser.add_argument('-m', '--message', type=str, help='Revision message')

    def handle(self, *args, **options):
        message = options.get('message')
        command = ['alembic', 'revision', '--autogenerate']
        if message:
            command.extend(['-m', message])

        logger.info(f'Running command: {" ".join(command)}')
        call(command)
        logger.info('Command executed successfully')