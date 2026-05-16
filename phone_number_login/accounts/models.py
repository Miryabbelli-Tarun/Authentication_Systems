from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=12,unique=True)
    username=models.CharField(max_length=50,unique=False,null=True,blank=True)

    USERNAME_FIELD='phone_number'

    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return self.phone_number