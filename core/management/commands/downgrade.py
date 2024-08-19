# core/management/commands/downgrade.py
from core.management.base import BaseCommand
from subprocess import call
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Run Alembic downgrade'

    def add_arguments(self, parser):
        parser.add_argument('revision', type=str, help='Revision to downgrade to')

    def handle(self, *args, **options):
        revision = options['revision']
        command = ['alembic', 'downgrade', revision]

        logger.info(f'Running command: {" ".join(command)}')
        call(command)
        logger.info('Command executed successfully')