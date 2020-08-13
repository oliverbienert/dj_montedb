import pytest

from config.tests.factories import AdultWithChildFactory


class TestAdult:
    @pytest.mark.django_db
    def test_adult_model(self):
        adult = AdultWithChildFactory()

        assert str(adult) == "Count Raven"
        assert len(adult.children.all()) == 1
        assert str(adult.children.first()) == "Lemmy Kilmister"
