from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    contact = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100, blank=False, null=False)



def __str__(self):
    return self.name
