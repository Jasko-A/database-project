from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from api.models import JokeRater

class User(AbstractUser):
    '''
    Subclassed django user model (inherits username, password, etc.)
    Has an optional one-to-one relationship with a joke rater/submitter.
    '''

    joke_rater = models.OneToOneField(JokeRater, null=True, blank=True)

    def __unicode__(self):
        return self.username