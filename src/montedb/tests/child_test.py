import datetime
import pytest

from .factories import ChildFactory
from testfixtures import Replace, test_date


class TestChild:
    @pytest.mark.django_db
    def test_child_model(self):
        child = ChildFactory(
            last_name="last name",
            first_name="first name",
            birth_date=datetime.date(2010, 1, 1),
            birth_place="place",
            care_time=2,
            kita=False
        )

        assert str(child) == "first name last name"
        with Replace('.factories.ChildFactory.date', test_date())
        assert child.age ==
