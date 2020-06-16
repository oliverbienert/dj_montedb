import datetime
import pytest

from .factories import PersonFactory


class TestPerson:
    @pytest.mark.django_db
    def test_person_model(self):
        person = PersonFactory(last_name="last name", first_name="first name", birth_date=datetime.date(2020, 1, 1))

        assert str(person) == "first name last name"
