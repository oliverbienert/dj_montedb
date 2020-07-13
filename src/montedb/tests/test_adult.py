from datetime import date

import pytest

from config.tests.factories import AdultFactory, ChildFactory


class TestAdult:
    @pytest.mark.django_db
    def test_adult_model(self):
        adult = AdultFactory(partner__partner=None)

        assert str(adult) == "first name last name"
        assert adult.partner.partner == adult
        assert adult.partner != adult
        assert len(adult.children.all()) == 1
