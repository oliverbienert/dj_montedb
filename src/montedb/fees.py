import pandas as pd

from .models import Income
from django.conf import settings


class ChildCalculation:
    income = None
    reduction1 = None
    reduction2 = None
    incomeApplied = None
    fee = None


class AdultCalculation:
    salary = None
    income = None
    unemployment = None
    other_payments = None
    deduction = None
    total_income = None

    def set_income(self, income):
        income_type = income.type
        income_amount = income.amount
        if income_type == Income.SALARY:
            self.salary = income_amount
        elif income_type == Income.INCOME:
            self.income = income_amount
        elif income_type == Income.UNEMPLOYMENT:
            self.unemployment = income_amount
        elif income_type == Income.OTHER_PAYMENTS:
            self.other_payments = income_amount
        elif income_type == Income.DEDUCTION:
            self.deduction = -income_amount
        else:
            print("WARNING: Income type {} is not known for AdultCalculation!".format(income_type))


class Fee:
    total_income = 0
    reduction2 = 0
    adults = set()
    children = set()
    payer = None
    adult_calculations = dict()
    children_calculations = dict()

    def __init__(self, adult):
        self.adults = get_adults(adult)
        self.children = get_children(adult)

        self.calc_total_income()
        self.calc_reduction2()
        self.calc_fee()

    def calc_total_income(self):
        for adult in self.adults:
            # TODO Should be chosen based on payer flag as soon as it is introduced
            self.payer = adult
            adult_calculation = AdultCalculation()
            adult_total_income = 0

            for income in adult.income.all():
                income_amount = income.amount
                if income.type == Income.DEDUCTION:
                    self.total_income -= income_amount
                    adult_total_income -= income_amount
                else:
                    self.total_income += income.amount
                    adult_total_income += income_amount
                adult_calculation.set_income(income)

            adult_calculation.total_income = adult_total_income
            self.adult_calculations[adult] = adult_calculation

    # TODO: Only childs getting child allowance are to be taken into account
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
        income = self.total_income
        for child in sorted(self.children, key=lambda x: x.birth_date):
            child_calculation = ChildCalculation()
            child_calculation.income = self.total_income
            fee = get_fee(income, child.kita, child.care_time)
            fee *= 1 - self.reduction2
            child_calculation.incomeApplied = income

            self.children_calculations[child] = child_calculation


def get_adults(adult):
    adults = set()
    for child in adult.children.all():
        # Only adults that have been marked as liable to pay for that child
        for related_adult in child.adults.filter(adultchild__liable=True):
            adults.add(related_adult)
    return adults


def get_children(adult):
    children = set()
    for child in adult.children.filter(adultchild__liable=True):
        children.add(child)
    return children


def get_fee(income, is_kita, care_time):
    if not is_kita:
        filename = settings['SCHOOL_FEE']
    elif care_time <= 6:
        filename = settings['KIGA_LE_30H_FEE']
    else:
        filename = settings['KIGA_GT_30H_FEE']
    df = pd.read_csv(filename)
