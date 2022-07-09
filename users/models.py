from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


SEX_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male'),
)


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, unique=True, null=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    personal_info = models.CharField(max_length=300, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(blank=True, null=True)

    REQUIRED_FIELDS = ['email', 'password']
