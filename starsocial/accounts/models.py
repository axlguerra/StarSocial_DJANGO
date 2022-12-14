from django.db import models
from django.contrib import auth
from django.contrib.auth.models import PermissionsMixin



class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        # string representation of user
        return '@{}'.format(self.username)


# Create your models here.
