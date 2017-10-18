from django.db import models
from django.conf import settings


CHAR_FIELD_MAX_LENGTH = 100
TEXT_FIELD_MAX_LENGTH = 1000


joke_categories = (
    ('medicine', 'Medicine/Doctor'),
    ('politics', 'Politics'),
    ('programming', 'Programming'),
    ('sports', 'Sports'),
    ('children', 'Children'),
    ('school', 'School'),
    ('animal', 'Animal'),
    ('lawyer', 'Lawyer'),
    ('math', 'Math'),
    ('nerd', 'Nerd'),
    ('chuck_norris', 'Chuck Norris')
)


joke_types = (
    ('question', 'Question'),
    ('pun', 'Pun'),
    ('one-liner', 'One-Liner'),
    ('dialogue', 'Dialogue')
)


class Joke(models.Model):
    '''
    Related fields: joke_ratings
    '''
    category = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, choices=joke_categories)
    joke_type = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, choices=joke_types)
    word_count = models.PositiveIntegerField()
    nsfw = models.BooleanField(default=False)
    subject = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    joke_text = models.TextField(max_length=TEXT_FIELD_MAX_LENGTH)

    def __unicode__(self):
        return 'Joke {0} | {1} | {2}'.format(self.id, self.category, self.joke_type)


class JokeRating(models.Model):
    '''
    '''
    joke = models.ForeignKey(Joke, related_name='joke_ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='joke_raters')
    rating = models.FloatField()
    would_recommend = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Joke Rating of {0} | {1} | {2}'.format(self.joke.id, self.rating, self.user)