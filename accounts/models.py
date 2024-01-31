from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(verbose_name = "User Nickname", max_length = 500, unique=True)
  email = models.EmailField(unique=True, blank=True)
  avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
  first_name = models.CharField(verbose_name="First Name User", max_length=50)
  last_name = models.CharField(verbose_name="Last Name User", max_length=50,  null=True, blank=True)
  date_of_birth = models.DateField(verbose_name="Date of Birth User", null=True, blank=True)
  STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    )
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
  address = models.CharField(max_length=500, blank=True)

    

  
  
