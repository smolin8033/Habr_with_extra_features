from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    personal_info = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    photo = models.ImageField(upload_to='users', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
