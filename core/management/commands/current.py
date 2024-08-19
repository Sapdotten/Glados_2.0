# core/management/commands/current.py
from core.management.base import BaseCommand
from subprocess import call
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Run Alembic current'

    def handle(self, *args, **options):
        command = ['alembic', 'current']

        logger.info(f'Running command: {" ".join(command)}')
        call(command)
        logger.info('Command executed successfully')