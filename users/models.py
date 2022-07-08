from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


SEX_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, unique=True)
    email = models.EmailField(unique=True, blank=True)
    personal_info = models.CharField(max_length=300)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.IntegerField(blank=True, null=True)
