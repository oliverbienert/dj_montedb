import csv

from montedb.models import ParentalContribution


def fill_parental_contribution_table():
    directory = "config/parental_contribution/"
    income_header = 'income'
    fee_types = [item[0] for item in ParentalContribution.CONTRIBUTION_TYPE]
    for fee_type in fee_types:
        filename = directory + fee_type + ".csv"
        try:
            file = open(filename)
        except FileNotFoundError:
            print("No configuration could be found for file {}.".format(filename))
        else:
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


def find_neighbours(value, df, col_name):
    exact_match = df[df[col_name] == value]
    if not exact_match.empty:
        return exact_match.index
    else:
        lower_neighbour_ind = df[df[col_name] < value][col_name].idxmax()
        upper_neighbour_ind = df[df[col_name] > value][col_name].idxmin()
        return [lower_neighbour_ind, upper_neighbour_ind] 