import pytest

from config.tests.factories import PhoneNumberFactory

from montedb.models import PhoneNumber


class TestPhoneNumber:
    @pytest.mark.django_db
    def test_phonenumber_model(self):
        phonenumber = PhoneNumberFactory()

        assert str(phonenumber.adult) == "Count Raven"
        assert phonenumber.type == PhoneNumber.PRIVATE
        assert phonenumber.phone_number == "+49123456789"
