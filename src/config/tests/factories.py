from datetime import date

import factory
from montedb.models import Address, Person, Child, Adult, AdultChild


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

    last_name = 'Hands'
    first_name = 'Idle'
    birth_date = date(2020, 1, 1)


class ChildFactory(factory.DjangoModelFactory):
    class Meta:
        model = Child

    last_name = 'Kilmister'
    first_name = 'Lemmy'
    birth_date = date(2010, 1, 1)
    birth_place = 'place'
    care_time = 2
    kita = False


class AdultFactory(factory.DjangoModelFactory):
    class Meta:
        model = Adult

    last_name = 'Raven'
    first_name = 'Count'
    birth_date = date(2010, 1, 1)
    iban = "DE123"
    address = factory.SubFactory(AddressFactory)
    club_member = True
    staff = False
    household_size = 5


class AdultChildFactory(factory.DjangoModelFactory):
    class Meta:
        model = AdultChild

    adult = factory.SubFactory(AdultFactory)
    child = factory.SubFactory(ChildFactory)
    kinship = AdultChild.FATHER
    liable = True
    max_contribution = False
    payer = True


class AdultWithChildFactory(AdultFactory):
    adult_child = factory.RelatedFactory(
        AdultChildFactory,
        factory_related_name='adult',
    )
