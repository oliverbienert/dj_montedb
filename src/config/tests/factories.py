import factory
from montedb.models import Address, Person


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person
