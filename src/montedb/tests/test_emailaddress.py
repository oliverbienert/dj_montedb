import pytest

from config.tests.factories import EmailAddressFactory

from montedb.models import EmailAddress


class TestEmailAddress:
    @pytest.mark.django_db
    def test_emailaddress_model(self):
        emailaddress = EmailAddressFactory()

        assert str(emailaddress.adult) == "Count Raven"
        assert emailaddress.type == EmailAddress.WORK
        assert emailaddress.email_address == "a@bc.de"
