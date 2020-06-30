from datetime import date

import factory
from montedb.models import Address, Person, Child


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
    birth_date = date(2020, 1, 1)


class ChildFactory(factory.DjangoModelFactory):
    class Meta:
        model = Child

    last_name = 'last name'
    first_name = 'first name'
    birth_date = date(2010, 1, 1)
    birth_place = 'place'
    care_time = 2
    kita = False