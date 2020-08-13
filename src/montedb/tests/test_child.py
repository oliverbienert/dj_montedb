from datetime import date

import pytest

from config.tests.factories import ChildFactory


class TestChild:
    @pytest.mark.django_db
    def test_child_model(self):
        child = ChildFactory(birth_date=date(2012, 1, 1))

        assert str(child) == "Lemmy Kilmister"
        assert child.age() == 8
