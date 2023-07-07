from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='file name of the file to be opened')
        parser.add_argument('-s','--sheet', type=str, help='sheetname of the file')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        sheetname = kwargs['sheet']

        print(filename)
        print(sheetname)