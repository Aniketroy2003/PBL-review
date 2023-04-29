from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    bg = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
    