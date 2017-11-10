from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django_countries.fields import CountryField

class User(AbstractUser):

    def __unicode__(self):
        return self.username