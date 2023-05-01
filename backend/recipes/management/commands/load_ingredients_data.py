from csv import DictReader

from django.core.management import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        if Ingredient.objects.exists():
            return
        for row in DictReader(open('./ingredients.csv')):
            ingredient = Ingredient(
                name=row['Name'], measurement_unit=row['Measurement_unit']
            )
            ingredient.save()
