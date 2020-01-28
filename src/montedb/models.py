import datetime

from django.db import models
from django.urls import reverse


class Address(models.Model):
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural='Addresses'

    def __str__(self):
        return '{} {}, {} {}'.format(self.street, self.house_number, self.zip_code, self.city)


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Child(Person):
    birth_place = models.CharField(max_length=255)
    care_time = models.IntegerField(null=False, default=4)
    kita = models.BooleanField()

    class Meta:
        verbose_name_plural='Children'

    def get_absolute_url(self):
        return reverse('montedb:child-update', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Adult(Person):
    iban = models.CharField(max_length=32)
    partner = models.OneToOneField("self", on_delete=models.SET_NULL, blank=True, null=True)
    address = models.ForeignKey(Address, related_name='adults', on_delete=models.SET_NULL,  blank=True, null=True)

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
    adult = models.ForeignKey(Adult, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    PARENT = "PR"
    KINSHIP = [
        (PARENT, 'Parent')
    ]
    kinship = models.CharField(max_length=2, choices=KINSHIP, default=PARENT)


class Income(models.Model):
    SALARY = 'salary'
    INCOME = 'income'
    UNEMPLOYMENT = 'unemployment'
    MAINTENANCE = 'maintenance'
    DEDUCTION = 'deduction'
    INCOME_TYPE = [
        (SALARY, 'Salary'),
        (INCOME, 'Income'),
        (UNEMPLOYMENT, 'Unemployment'),
        (MAINTENANCE, 'Maintenance'),
        (DEDUCTION, 'Deduction')
    ]
    amount = models.IntegerField()
    type = models.CharField(
        max_length=20,
        choices=INCOME_TYPE,
        default=SALARY
    )
    adult = models.ForeignKey(Adult, models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.type, self.amount)

