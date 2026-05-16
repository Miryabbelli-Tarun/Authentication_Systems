from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from accounts.manager import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone_number=models.CharField(max_length=100,unique=True)
    username=models.CharField(max_length=100,unique=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects=CustomUserManager()
    def __str__(self):
        return self.phone_number