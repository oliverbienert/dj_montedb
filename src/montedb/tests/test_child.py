from datetime import date

import pytest

from config.tests.factories import ChildFactory


class TestChild:
    @pytest.mark.django_db
    def test_child_model(self):
        child = ChildFactory(birth_date = date(2010, 1, 1))

        assert str(child) == "first name last name"
        assert child.age() == 10
