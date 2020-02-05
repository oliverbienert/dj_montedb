import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    street = models.CharField(_('Street'), max_length=255)
    house_number = models.CharField(_('House number'), max_length=255, blank=True, null=True)
    zip_code = models.CharField(_('ZIP code'), max_length=255)
    city = models.CharField(_('City'), max_length=255)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return '{} {}, {} {}'.format(self.street, self.house_number, self.zip_code, self.city)


class Person(models.Model):
    last_name = models.CharField(_('Last name'), max_length=255)
    first_name = models.CharField(_('First name'), max_length=255)
    birth_date = models.DateField(_('Birth date'), default=datetime.date.today)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Child(Person):
    birth_place = models.CharField(_('Birth place'), max_length=255)
    care_time = models.IntegerField(_('Care time'), null=False, default=4)
    kita = models.BooleanField(_('Day-care centre'))

    class Meta:
        verbose_name = _('Child')
        verbose_name_plural = _('Children')

    def get_absolute_url(self):
        return reverse('montedb:child-update', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Adult(Person):
    iban = models.CharField('IBAN', max_length=32)
    partner = models.OneToOneField('self', verbose_name=_('Partner'), on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(Address, verbose_name=_('Address'), related_name='adults', on_delete=models.SET_NULL,
                                blank=True, null=True)
    children = models.ManyToManyField(Child, through='AdultChild', verbose_name=_('Children'))
    club_member = models.BooleanField(_('Club member'), default=False)
    staff = models.BooleanField(_('Staff'), default=False)
    household_size = models.IntegerField(_('Household size'), null=True, blank=True,
                                         validators=[MaxValueValidator(10), MinValueValidator(1)])

    class Meta:
        verbose_name = _('Adult')
        verbose_name_plural = _('Adults')

    def save(self, recursive=True, *args, **kwargs):
        super(Person, self).save()
        if self.partner is None:
            Adult.objects.all().filter(partner=self).update(partner=None)
        else:
            self.partner.partner = self
            if recursive:
                self.partner.save(recursive=False)

    def get_absolute_url(self):
        return reverse('montedb:adult-update', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class AdultChild(models.Model):
    MOTHER = 'mother'
    FATHER = 'father'
    GRANDMOTHER = 'grandmother'
    GRANDFATHER = 'grandfather'
    OTHER = 'other'
    KINSHIP_TYPE = [
        (MOTHER, _('Mother')),
        (FATHER, _('Father')),
        (GRANDMOTHER, _('Grandmother')),
        (GRANDMOTHER, _('Grandfather')),
        (OTHER, _('Other'))
    ]
    adult = models.ForeignKey(Adult, on_delete=models.CASCADE, verbose_name=_('Adult'))
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name=_('Child'))
    kinship = models.CharField(_('Degree of kinship'), max_length=20, choices=KINSHIP_TYPE, default=MOTHER)
    liable = models.BooleanField(_('Liable to contribution'), default=False)
    payer = models.BooleanField(_('Payer'), default=False)

    class Meta:
        verbose_name = _('Degree of kinship')
        verbose_name_plural = _('Degrees of kinship')
        unique_together = (('adult', 'child',), ('child', 'kinship',),)


class Income(models.Model):
    SALARY = 'salary'
    INCOME = 'income'
    UNEMPLOYMENT = 'unemployment'
    MAINTENANCE = 'maintenance'
    DEDUCTION = 'deduction'
    INCOME_TYPE = [
        (SALARY, _('Salary')),
        (INCOME, _('Income')),
        (UNEMPLOYMENT, _('Unemployment')),
        (MAINTENANCE, _('Maintenance')),
        (DEDUCTION, _('Deduction'))
    ]
    amount = models.IntegerField(_('Amount'))
    type = models.CharField(
        _('Type'),
        max_length=20,
        choices=INCOME_TYPE,
        default=SALARY
    )
    adult = models.ForeignKey(Adult, models.CASCADE, verbose_name=_('Adult'))

    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')

    def __str__(self):
        return "{}: {}".format(self.type, self.amount)


class PhoneNumber(models.Model):
    PRIVATE = 'privat'
    WORK = 'work'
    MOBILE = 'mobile'
    FAX = 'fax'
    FON_NUMBER_TYPE = [
        (PRIVATE, _('Private')),
        (WORK, _('Work')),
        (MOBILE, _('Mobile')),
        (FAX, _('Fax'))
    ]
    phone_number = PhoneNumberField(_('Phone number'))
    type = models.CharField(
        _('Type'),
        max_length=10,
        choices=FON_NUMBER_TYPE,
        default=PRIVATE
    )
    adult = models.ForeignKey(Adult, models.CASCADE, verbose_name=_('Adult'))

    class Meta:
        verbose_name = _('Phone number')
        verbose_name_plural = _('Phone numbers')
        unique_together = (('adult', 'phone_number'),)


class EmailAddress(models.Model):
    PRIVATE = 'private'
    WORK = 'work'
    EMAIL_ADDRESS_TYPE = [
        (PRIVATE, _('Private')),
        (WORK, _('Work')),
    ]
    email_address = models.EmailField(_('E-Mail address'))
    type = models.CharField(
        _('Type'),
        max_length=10,
        choices=EMAIL_ADDRESS_TYPE,
        default=PRIVATE
    )
    adult = models.ForeignKey(Adult, models.CASCADE, verbose_name=_('Adult'))

    class Meta:
        verbose_name = _('E-Mail address')
        verbose_name_plural = _('E-Mail addresses')
        unique_together = (('adult', 'email_address'),)


class Ruling(models.Model):
    EXTENDED_DAY_TIME = 'ext_day_time'
    EXTENDED_CARE_TIME = 'ext_care_time'
    RIGHT_TO_REQUEST = 'right_to_request'
    FEE_PAYMENT_BY_COUNTY = 'fee_by_county'
    LUNCH_PAYMENT_BY_COUNTY = 'lunch_by_county'
    RULING_TYPE = [
        (EXTENDED_DAY_TIME, _('Extended day time')),
        (EXTENDED_CARE_TIME, _('Extended care time')),
        (RIGHT_TO_REQUEST, _('Right to request and vote (available care service)')),
        (FEE_PAYMENT_BY_COUNTY, _('Fee payment by county')),
        (LUNCH_PAYMENT_BY_COUNTY, _('Lunch payment by county'))

    ]
    type = models.CharField(
        _('Ruling type'),
        max_length=10,
        choices=RULING_TYPE,
    )
    valid_from = models.DateField(_('Valid from'), default=datetime.date.today)
    valid_to = models.DateField(_('Valid to'), default=datetime.date.today)
    # document = models.FileField(_('Document'), upload_to="documents/")
    child = models.ForeignKey(Child, models.CASCADE, verbose_name=_('Child'))

    class Meta:
        verbose_name = _('Ruling')
        verbose_name_plural = _('Rulings')

