from pytest_factoryboy import register

from config.tests.factories import AddressFactory, PersonFactory

register(AddressFactory)
register(PersonFactory)