import pytest
from pytest_factoryboy import register, LazyFixture

from . import factories

register(factories.AddressFactory)
register(factories.PersonFactory)
register(factories.ChildFactory)
register(factories.IncomeFactory)
register(factories.EmailAddressFactory)
register(factories.PhoneNumberFactory)
register(factories.RulingFactory)
register(factories.ParentalContributionFactory)
register(factories.AdultChildFactory)
register(factories.AdultWithChildFactory, partner=LazyFixture('second_adult'))
register(factories.AdultWithChildFactory, 'second_adult', last_name='Amarth', first_name='Amon')

