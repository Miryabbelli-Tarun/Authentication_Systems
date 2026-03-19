
from django.contrib.auth.models import BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extrafields):
        if not email:
            raise ValueError('email must be required')
        user=self.model(email=email,**extrafields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password=None,**extrafields):
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_active',True)
        extrafields.setdefault('is_staff',True)

        return self.create_user(email,password,**extrafields)