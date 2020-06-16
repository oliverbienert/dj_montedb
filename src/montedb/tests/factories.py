import factory
from ..models import Address, Person


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person
