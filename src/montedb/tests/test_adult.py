from datetime import date

import pytest

from config.tests.factories import AdultFactory, ChildFactory, AdultWithChildFactory


class TestAdult:
    @pytest.mark.django_db
    def test_adult_model(self):
        adult = AdultWithChildFactory(partner__partner=None)

        assert str(adult) == "first name last name"
        assert adult.partner.partner == adult
        assert adult.partner != adult
        assert len(adult.children.all()) == 1
        assert str(adult.children.first()) == "first name last name"
