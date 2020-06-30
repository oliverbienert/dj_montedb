from datetime import date

import factory
from montedb.models import Address, Person, Child


class AddressFactory(factory.DjangoModelFactory):
    class Meta:
        model = Address


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = Person


class ChildFactory(factory.DjangoModelFactory):
    class Meta:
        model = Child

    last_name = 'last name'
    first_name = 'first name'
    birth_date = date(2010, 1, 1)
    birth_place = 'place'
    care_time = 2
    kita = False