from typing import Any, Optional
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, Group, Permission, User


class CustomUserManager(UserManager):
    def create_user(self,email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('Email field is empty')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

class ProfileChoises(models.TextChoices):
    customer = 'customer'
    employee = 'employee'
    business = 'business'


class CustomUser(AbstractBaseUser):
    is_superuser = models.BooleanField()
    groups = models.ManyToManyField(Group)
    user_permissions = models.ManyToManyField(Permission)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_created=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, blank=True)
    # USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    profile = models.CharField(default='customer', choices=ProfileChoises.choices)

    objects = CustomUserManager()
    


# check
    def __str__(self) -> str:
        return self.get_email_field_name()
    
