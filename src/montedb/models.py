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

