from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    """Book Model"""
    name = models.CharField(max_length=256,)
    author = models.CharField(max_length=256)
    genre = models.CharField(max_length=126)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})

class CustomUser(AbstractUser):
    """User Model"""
    email = models.EmailField(unique=True,)
    username=None
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []





