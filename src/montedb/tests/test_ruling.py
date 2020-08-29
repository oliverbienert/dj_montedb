import pytest

from datetime import date

from config.tests.factories import RulingFactory

from montedb.models import Ruling


class TestRuling:
    @pytest.mark.django_db
    def test_ruling_model(self):
        ruling = RulingFactory()

        assert str(ruling.child) == "Lemmy Kilmister"
        assert ruling.type == Ruling.EXTENDED_DAY_TIME
        assert ruling.valid_from == date(2020, 1, 1)
        assert ruling.valid_to == date(2021, 1, 1)
