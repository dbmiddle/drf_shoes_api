from django.core.management.base import BaseCommand, CommandError
from demo.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = 'Populates shoe type and shoe color details in respective data tables'

    def handle(self, *args, **options):
        # shoe_color = ShoeColor.objects.all()
        styles = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        colors = ['RE', 'OR', 'YE', 'GR',
                  'BLU', 'IN', 'VI', 'WH', 'BLK']
        for shoetype in styles:
            ShoeType.objects.create(
                style=shoetype
            )
        for shoecolor in colors:
            ShoeColor.objects.create(
                color_name=shoecolor
            )
