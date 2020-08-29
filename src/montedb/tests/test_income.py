import pytest

from config.tests.factories import IncomeFactory

from montedb.models import Income


class TestIncome:
    @pytest.mark.django_db
    def test_income_model(self):
        income = IncomeFactory()

        assert str(income.adult) == "Count Raven"
        assert income.type == Income.SALARY
        assert income.amount == 1234
