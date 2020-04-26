import argparse
import csv
import os

from django.core.management.base import BaseCommand

from ...models import ParentalContribution


class Command(BaseCommand):
    help = "Reads in all .csv-Files matching the format in config/parental_contribution as a parental contribution " \
           "table. "
    directory = "config/parental_contribution"

    def handle(self, *args, **options):
        income_header = 'income'
        fee_types = [item[0] for item in ParentalContribution.CONTRIBUTION_TYPE]
        for filename in os.scandir(self.directory):
            if not filename.path.endswith(".csv"):
                continue
            with open(filename) as file:
                fee_type = next(file)
                if fee_type.rstrip() not in fee_types:
                    print("Contribution type {} in file {} is not valid.".format(fee_type, filename))
                    continue
                reader = csv.DictReader(file, delimiter=',')
                fieldnames = reader.fieldnames
                # Checking if the file specifies the right header, consisting of:
                # income
                if len(fieldnames) == 0:
                    print("No header was given in file {}.".format(filename))
                    continue
                if fieldnames[0] != income_header:
                    print("Header for file {} does not start with 'income'".format(filename))
                    continue
                i = 1
                # and an ascending number
                for header in fieldnames[1:]:
                    try:
                        if i != int(header):
                            print("Header entry {} is not {} as expected for file {}".format(header, i, filename))
                            continue
                        i += 1
                    except ValueError:
                        print("Header entry {} cannot be parsed as int for file {}.".format(header, filename))
                        continue
                print("Reading file {}".format(filename))
                for row in reader:
                    income = row[income_header]
                    for children in range(1, i):
                        contribution = row[str(children)]
                        contribution_entry, created = ParentalContribution.objects.get_or_create(
                            type=fee_type,
                            income=income,
                            children=children,
                            defaults={'contribution': contribution}
                        )
                        if not created:
                            contribution_entry.contribution = contribution
                            contribution_entry.save()
