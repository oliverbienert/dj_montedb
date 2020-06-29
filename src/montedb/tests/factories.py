import factory
from ..models import Address, Child, Person


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person


class ChildFactory(factory.DjangoModelFactory):
    class Meta:
        model = Child
