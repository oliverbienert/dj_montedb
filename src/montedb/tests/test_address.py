import pytest

from config.tests.factories import AddressFactory


class TestAddress:
    @pytest.mark.django_db
    def test_address_model(self):
        address = AddressFactory(street="Street", house_number="1", zip_code="12345", city="City")

        assert str(address) == "Street 1, 12345 City"
