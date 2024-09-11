from django.db import models # type: ignore
from datetime import datetime


class KYC(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name='Date of Birth') #This is the name of the model field. It stands for "Date of Birth" and will be used as the attribute name when you reference this field in your model instance 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=255, verbose_name='State / District')
    town = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone1 = models.CharField(max_length=15, verbose_name='Phone Number 1')
    phone2 = models.CharField(max_length=15, verbose_name='Phone Number 2', blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

