from django.db import models
from django.conf import settings


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
    ('chuck_norris', 'Chuck Norris'),
    ('dad', 'Dad')
)


joke_types = (
    ('question', 'Question'),
    ('pun', 'Pun'),
    ('one-liner', 'One-Liner'),
    ('dialogue', 'Dialogue'),
    ('pickup_line', 'Pick Up Line'),
    ('punch_line', 'Punch line'),
    ('fun_fact', 'Fun Fact'),
    ('other', 'Other')
)


joke_lengths = (
    ('short', 'Short'),
    ('medium', 'Medium'),
    ('long', 'Long')
)


class Joke(models.Model):
    '''
    Related fields: joke_ratings
    '''
    category = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, choices=joke_categories)
    joke_type = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH, choices=joke_types)
    joke_length = models.CharField(default='short', max_length=settings.CHAR_FIELD_MAX_LENGTH, choices=joke_lengths)
    nsfw = models.BooleanField(default=False)
    subject = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    joke_text = models.TextField(max_length=settings.TEXT_FIELD_MAX_LENGTH)

    def __unicode__(self):
        return 'Joke {0} | {1} | {2}'.format(self.id, self.category, self.joke_type)

    def get_current_rating(self):
        ''' Get mean rating of a joke. Returns an int or string. '''
        from api.models import JokeRating

        joke_ratings = JokeRating.objects.filter(joke=self)

        if joke_ratings.count():
            avg = 0.0
            for jrating in joke_ratings:
                avg += jrating.rating
            return avg / joke_ratings.count()
        else:
            return "Not yet rated."


class JokeRating(models.Model):
    '''
    '''
    joke = models.ForeignKey(Joke, related_name='joke_ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='joke_raters')
    rating = models.PositiveIntegerField(default=0, choices=(
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5)
        ))
    would_recommend = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Joke Rating of {0} | {1} | {2}'.format(self.joke.id, self.rating, self.user)
