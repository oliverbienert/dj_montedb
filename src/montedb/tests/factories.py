import factory
from ..models import Address


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address
