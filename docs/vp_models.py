# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'address'


class Adult(models.Model):
    id = models.ForeignKey('Person', models.DO_NOTHING, db_column='id')
    iban = models.CharField(max_length=34, blank=True, null=True)
    partner = models.ForeignKey('self', models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    club_member = models.BooleanField()
    household_size = models.SmallIntegerField(blank=True, null=True)
    staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'adult'


class AdultChild(models.Model):
    adult = models.ForeignKey(Adult, models.DO_NOTHING)
    child = models.ForeignKey('Child', models.DO_NOTHING)
    kinship = models.CharField(max_length=255)
    liable = models.BooleanField()
    payer = models.BooleanField()
    max_contribution = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'adult_child'


class Child(models.Model):
    id = models.ForeignKey('Person', models.DO_NOTHING, db_column='id')
    birthplace = models.CharField(max_length=255)
    care_time = models.TextField()  # This field type is a guess.
    kita = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'child'


class EmailAddress(models.Model):
    email_address = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    adult = models.ForeignKey(Adult, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_address'
        unique_together = (('id', 'email_address'),)


class Income(models.Model):
    amount = models.IntegerField()
    type = models.CharField(max_length=255)
    adult = models.ForeignKey(Adult, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'income'


class ParentalContribution(models.Model):
    income = models.IntegerField()
    type = models.CharField(max_length=20)
    children = models.SmallIntegerField()
    contribution = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'parental_contribution'


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'person'


class PhoneNumber(models.Model):
    phone_number = models.IntegerField()
    type = models.CharField(max_length=255)
    adult = models.ForeignKey(Adult, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'phone_number'
        unique_together = (('id', 'phone_number'),)


class Ruling(models.Model):
    child = models.ForeignKey(Child, models.DO_NOTHING)
    type = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_to = models.DateField()
    document = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruling'
