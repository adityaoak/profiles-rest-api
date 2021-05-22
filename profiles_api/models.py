from django.db import models
from django.contrib.auth.models import AbstractBaseUser  #added new
from django.contrib.auth.models import PermissionsMixin   #added new
from django.contrib.auth.models import BaseUserManager   #added new
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        # Emails can be case sensitive for the first half of the string and case-insensetive for the rest half. Thus normalization is required
        # Gmail and hotmail make entire email address case insensetive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  #To encrypt password and store as hashed instead of clear text
        user.save(using=self._db)  #To enable support for multiple databases for future use

        return user

    def create_super_user(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True  #is_superuser not defined in UserProfile since it is automatically created by the PermissionMixin
        user.is_staff = True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # specify model manager we're gonna use
    objects = UserProfileManager()

    # additional required fields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # some functions used for django to interact with customer user model
    def get_full_name(self):  # since we're defining function inside of class, self is required
        """Restrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
