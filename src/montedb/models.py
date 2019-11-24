from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField

    def __str__(self):
        return "Person (First name: {}, Last name: {}, Birth date: {}".format(
            self.first_name,
            self.last_name,
            self.birth_date
        )


class Child(Person):
    birth_place = models.CharField(max_length=255)
    care_time = models.DurationField
    kita = models.BooleanField
