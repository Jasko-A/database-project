from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django_countries.fields import CountryField
from api.models import joke_types, joke_categories

class User(AbstractUser):

    # gender = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LENGTH, choices=(
    #         ('male', 'Male'),
    #         ('female', 'Female'),
    #         ('other', 'Other')
    #     ))

    # ethnicities picked from https://www.opm.gov/forms/pdf_fill/sf181.pdf
    ethnicity = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True, choices=(
            ('american_indian_alaskan', 'American Indian or Alaska Native'),
            ('asian', 'Asian'),
            ('black_or_african_american', 'Black or African American'),
            ('hawaiian_or_pacific_islander', 'Hawaiian or Other Pacific Islander'),
            ('white', 'White')
        ))

    pref_joke_type1 = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True, choices=joke_types)
    pref_joke_type2 = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True, choices=joke_types)
    pref_joke_type3 = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True, choices=joke_types)

    pref_joke_category = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True, choices=joke_categories)

    country_of_origin = CountryField(blank=True, blank_label='(select country)')

    birth_date = models.DateField(null=True, blank=True)
    major = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, blank=True)

    def __unicode__(self):
        return self.username