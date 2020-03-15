import argparse, csv
from django.core.management.base import BaseCommand, CommandError

from ...models import ParentalContribution


class Command(BaseCommand):
    help = "Reads in a specified .csv-File as a parental contribution table."

    def add_arguments(self, parser):
        parser.add_argument('--type', choices=[types[0] for types in ParentalContribution.CONTRIBUTION_TYPE])
        parser.add_argument('--file', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        type = options['type']
        file = options['file']
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            income = row['income']
            for children in [1, 2, 3, 4]:
                contribution = row[str(children)]
                contributionEntry, created = ParentalContribution.objects.get_or_create(
                    type=type,
                    income=income,
                    children=children,
                    defaults={'contribution': contribution}
                )
                if not created:
                    contributionEntry.contribution = contribution
                    contributionEntry.save()
