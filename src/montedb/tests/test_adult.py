import pytest

from config.tests.factories import AdultWithChildFactory


class TestAdult:
    @pytest.mark.django_db
    def test_adult_model(self):
        adult = AdultWithChildFactory()
        adult2 = AdultWithChildFactory(last_name="Amarth", first_name="Amon")
        adult.partner = adult2

        assert str(adult) == "Count Raven"
        assert len(adult.children.all()) == 1
        assert str(adult.children.first()) == "Lemmy Kilmister"

        assert str(adult2) == "Amon Amarth"
        assert str(adult.partner.partner == adult)
