import pytest

from config.tests.factories import PersonFactory


class TestPerson:
    @pytest.mark.django_db
    def test_person_model(self):
        person = PersonFactory()

        assert str(person) == "first name last name"
