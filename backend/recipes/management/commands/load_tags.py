import csv
import os

from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
                os.path.join(settings.DATA_ROOT, 'tags.csv'),
                encoding='utf-8'
        ) as file:
            reader = csv.DictReader(file)
            Tag.objects.bulk_create(
                Tag(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Tags added'))
