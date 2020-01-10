import datetime

from django.db import models
from django.urls import reverse


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "Person (First name: {}, Last name: {}, Birth date: {}".format(
            self.first_name,
            self.last_name,
            self.birth_date
        )


class Child(Person):
    birth_place = models.CharField(max_length=255)
    care_time = models.IntegerField(null=False, default=4)
    kita = models.BooleanField()

    def get_absolute_url(self):
        return reverse('child-update', kwargs={'pk': self.pk})

    def __str__(self):
        return "Child (" \
               "First name: {}, " \
               "Last name: {}, " \
               "Birth date: {}, " \
               "Birth place: {}, " \
               "Care time:  {}, " \
               "Kita: {}".format(
            self.first_name,
            self.last_name,
            self.birth_date,
            self.birth_place,
            self.care_time,
            self.kita)


class Adult(Person):
    iban = models.CharField(max_length=32)
    partner = models.OneToOneField("self", on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, recursive=True, *args, **kwargs):
        super(Person, self).save()
        if self.partner is not None and recursive:
            self.partner.partner = self
            self.partner.save(recursive=False)

    def get_absolute_url(self):
        return reverse('adult-update', kwargs={'pk': self.pk})

    def __str__(self):
        return "Adult(" \
               "First name: {}, " \
               "Last name: {}, " \
               "Birth date: {}, " \
               "IBAN: {}".format(
            self.first_name,
            self.last_name,
            self.birth_date,
            self.iban)