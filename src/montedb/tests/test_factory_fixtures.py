import pytest

from datetime import date


@pytest.mark.django_db
class TestFactoryFixtures:

    def test_address(self, address_factory):
        address = address_factory()
        assert str(address) == "Street 1, 12345 City"

    def test_person(self, person_factory):
        person = person_factory()
        assert str(person) == "Idle Hands"

    def test_child(self, child_factory):
        child = child_factory(birth_date=date(2012, 1, 1))
        assert str(child) == "Lemmy Kilmister"
        assert child.age() == 8

    def test_income(self, income_factory):
        income = income_factory()
        assert str(income.adult) == "Count Raven"
        assert income.type == income.SALARY
        assert income.amount == 1234

    def test_email_address(self, email_address_factory):
        email_address = email_address_factory()
        assert str(email_address.adult) == "Count Raven"
        assert email_address.type == email_address.WORK
        assert email_address.email_address == "a@bc.de"

    def test_phone_number(self, phone_number_factory):
        phone_number = phone_number_factory()
        assert str(phone_number.adult) == "Count Raven"
        assert phone_number.type == phone_number.PRIVATE
        assert phone_number.phone_number == "+49123456789"

    def test_ruling(self, ruling_factory):
        ruling = ruling_factory()
        assert str(ruling.child) == "Lemmy Kilmister"
        assert ruling.type == ruling.EXTENDED_DAY_TIME
        assert ruling.valid_from == date(2020, 1, 1)
        assert ruling.valid_to == date(2021, 1, 1)

    def test_parental_contribution(self, parental_contribution_factory):
        contribution = parental_contribution_factory()
        assert contribution.type == contribution.SCHOOL_FEE
        assert contribution.income == 1234
        assert contribution.children == 1
        assert contribution.contribution == 56

    def test_adult_with_child(self, adult_with_child_factory):
        adult = adult_with_child_factory()
        assert str(adult) == "Count Raven"
