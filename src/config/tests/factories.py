import datetime
import factory
from montedb.models import Address, Person


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address

    street = 'Street'
    house_number = '1'
    zip_code = '12345'
    city = 'City'


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person

    last_name = 'last name'
    first_name = 'first name'
    birth_date = datetime.date(2020, 1, 1)