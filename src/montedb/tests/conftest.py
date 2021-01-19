import pytest
import pandas as pd
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


@pytest.fixture
def df_school_fee():
    lst = []
    income = 1000
    for _ in range(25):
        fee = income / 10
        fee2 = fee * .8
        fee3 = fee * .6
        lst.append((income, fee, fee2, fee3,))
        income = income + 200
    columns = ['income', '1', '2', '3']
    return pd.DataFrame(lst, columns = columns)