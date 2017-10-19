from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):

	gender = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LENGTH, choices=(
			('male', 'Male'),
			('female', 'Female'),
			('other', 'Other')
		))

	birth_date = models.DateField(null=True, blank=True)
	major = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True)
	birth_country = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True)
	ethnicity = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True)
	
	def __unicode__(self):
		return self.username