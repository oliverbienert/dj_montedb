from django.core.management.base import BaseCommand

from config.utils import fill_parental_contribution_table


class Command(BaseCommand):
    help = "Reads in all .csv-Files matching the format in config/parental_contribution as a parental contribution " \
           "table. "

    def handle(self, *args, **options):
        fill_parental_contribution_table()