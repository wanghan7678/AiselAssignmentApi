from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from .usermanager import CustomUserManager

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45)
    dob = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.CharField(max_length=100, null=True)
    comments = models.CharField(max_length=200, null=True)

class User(AbstractBaseUser, PermissionsMixin):
    # Roles field:
    ADMIN = 1
    READER = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (READER, 'Reader')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=2)
    added_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email