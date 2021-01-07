import logging

import pytest
from pytest_factoryboy import LazyFixture

from montedb.fees import Fee
from montedb.models import ParentalContribution

logger = logging.getLogger('project')


@pytest.mark.django_db
class TestAdult:

    def test_adult_model(self, adult, second_adult):
        assert str(adult) == "Count Raven"
        assert len(adult.children.all()) == 1
        assert str(adult.children.first()) == "Lemmy Kilmister"
        assert str(adult.adultchild_set.first().kinship) == "father"

        assert str(second_adult) == "Amon Amarth"
        assert str(adult.partner.partner == adult)

    # noinspection PyTestParametrized
    @pytest.mark.parametrize("income__adult", [LazyFixture(lambda adult: adult)])
    def test_school_fee(self, adult, income):
        fee = Fee(adult)
        assert income.adult == adult
        assert fee.children_calculations[0].fee == 250
