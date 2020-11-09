import pytest


@pytest.mark.django_db
class TestAdult:

    def test_adult_model(self, adult, second_adult):
        assert str(adult) == "Count Raven"
        assert len(adult.children.all()) == 1
        assert str(adult.children.first()) == "Lemmy Kilmister"
        assert str(adult.adultchild_set.first().kinship) == "father"

        assert str(second_adult) == "Amon Amarth"
        assert str(adult.partner.partner == adult)
