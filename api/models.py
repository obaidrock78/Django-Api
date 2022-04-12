from django.db import models


# Create your models here.



class Phone(models.Model):
    phone = models.CharField(max_length=10)
    internal_address = models.CharField(max_length=8)


class Person(models.Model):
    fl_name = models.CharField(max_length=100)
    rooms = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    internal_address = models.CharField(max_length=8)
    section = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.fl_name}{self.section}"
