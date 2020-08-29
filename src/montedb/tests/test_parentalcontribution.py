import pytest

from datetime import date

from config.tests.factories import ParentalContributionFactory

from montedb.models import ParentalContribution


class TestParentalContribution:
    @pytest.mark.django_db
    def test_parentalcontribution_model(self):
        contribution = ParentalContributionFactory()

        assert contribution.type == ParentalContribution.SCHOOL_FEE
        assert contribution.income == 1234
        assert contribution.children == 1
        assert contribution.contribution == 56
