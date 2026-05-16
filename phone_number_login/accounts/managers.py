
from django.contrib.auth.models import BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self,phone_number,password,**extra_fields):
        if not phone_number:
            raise ValueError('phone number must be required')
        user=self.create(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,phone_number,password,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(phone_number,password,**extra_fields)
