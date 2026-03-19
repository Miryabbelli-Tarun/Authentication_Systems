from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.manager import CustomUserManager
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(max_length=40,unique=True)
    username=models.CharField(max_length=100,unique=False,blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email