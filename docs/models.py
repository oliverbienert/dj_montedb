# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'addresses'


class Adults(models.Model):
    id = models.ForeignKey('Persons', models.DO_NOTHING, db_column='id')
    iban = models.CharField(max_length=34, blank=True, null=True)
    partner_to = models.ForeignKey('self', models.DO_NOTHING, db_column='partner_to')

    class Meta:
        managed = False
        db_table = 'adults'


class AdultsChildren(models.Model):
    adult = models.ForeignKey(Adults, models.DO_NOTHING)
    child = models.ForeignKey('Children', models.DO_NOTHING)
    kinship = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'adults_children'


class Children(models.Model):
    id = models.ForeignKey('Persons', models.DO_NOTHING, db_column='id')
    birthplace = models.CharField(max_length=255)
    care_time = models.TextField()  # This field type is a guess.
    kita = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'children'


class EmailAddresses(models.Model):
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'email_addresses'
        unique_together = (('id', 'email'),)


class Income(models.Model):
    amount = models.IntegerField()
    type = models.CharField(max_length=255)
    adult = models.ForeignKey(Adults, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'incomes'


class Persons(models.Model):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'persons'


class PersonsAddresses(models.Model):
    address = models.ForeignKey(Addresses, models.DO_NOTHING)
    person = models.ForeignKey(Persons, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'persons_addresses'


class PersonsEmailAddresses(models.Model):
    email_address = models.ForeignKey(EmailAddresses, models.DO_NOTHING)
    person = models.ForeignKey(Persons, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'persons_email_addresses'


class PersonsPhoneNumbers(models.Model):
    phone_number = models.ForeignKey('PhoneNumbers', models.DO_NOTHING)
    person = models.ForeignKey(Persons, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'persons_phone_numbers'


class PhoneNumbers(models.Model):
    fonnumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phone_numbers'
        unique_together = (('id', 'fonnumber'),)


class Rulings(models.Model):
    type = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_to = models.DateField()
    document = models.CharField(max_length=255, blank=True, null=True)
    child = models.ForeignKey(Children, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rulings'
