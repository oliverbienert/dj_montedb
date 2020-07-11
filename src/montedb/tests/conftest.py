from pytest_factoryboy import register

from config.tests.factories import AddressFactory, PersonFactory, ChildFactory

register(AddressFactory)
register(PersonFactory)
register(ChildFactory)