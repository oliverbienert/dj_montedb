from .models import Adult, Income, ParentalContribution


def get_adults(adult):
    adults = set()
    for child in adult.children.all():
        for related_adult in child.adults.all():
            adults.add(related_adult)
    return adults


def get_children(adult):
    children = set()
    for child in adult.children.all():
        children.add(child)
    return children


class Fee:
    total_income = 0
    reduction2 = 0
    adults = set()
    children = set()

    def calc(self, adult):
        self.adults = get_adults(adult)
        self.children = get_children(adult)
        self.calc_total_income()
        self.calc_reduction2()
        return self.calc_fee()

    def calc_total_income(self):
        for adult in self.adults:
            for income in adult.income.all():
                if income.type == Income.DEDUCTION:
                    self.total_income -= income.amount
                else:
                    self.total_income += income.amount

    def calc_reduction2(self):
        total = len(self.adults) + len(self.children)
        household_size = 0
        for adult in self.adults:
            size = adult.household_size
            try:
                household_size = max(household_size, size)
            except (ValueError, TypeError):
                pass
        if total < household_size:
            add_household_members = household_size - total
            self.reduction2 = add_household_members * 0.05

    def calc_fee(self):
        reduction1 = 0
        result = dict()
        for child in sorted(self.children, key=lambda x: x.birth_date):
            income = self.total_income
            # 20 % reduction for each further child
            income *= 1 - reduction1
            reduction1 += 0.2
            # Apply reduction2 (5% reduction per additional household member not in school)
            income *= 1 - self.reduction2

            contribution = ParentalContribution.objects.order_by('-income').filter(
                income__lte=income,
                type=ParentalContribution.SCHOOL_FEE,
                children=len(self.children))[0]

            result[child] = contribution.contribution

        return result

