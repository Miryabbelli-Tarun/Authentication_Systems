from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from accounts.manager import CustomUserManager
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=100,blank=True,null=True)
    is_staff=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email
    