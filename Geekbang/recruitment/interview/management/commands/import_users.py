import csv

from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'import users data from a CSV file to the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f, dialect='excel', delimiter=',')
            reader = list(reader)
            for row in reader[1:]:
                user = User.objects.create(
                    username=row[0],
                    email=row[1],
                    first_name=row[2],
                    last_name=row[3],
                )
