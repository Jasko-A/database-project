from django.db import models
from django.conf import settings


JOKE_CATEGORIES = (
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

JOKE_TYPES = (
    ('question', 'Question'),
    ('pun', 'Pun'),
    ('one-liner', 'One-Liner'),
    ('dialogue', 'Dialogue'),
    ('pickup_line', 'Pick Up Line'),
    ('punch_line', 'Punch line'),
    ('fun_fact', 'Fun Fact'),
    ('other', 'Other')
)


class Joke(models.Model):
    '''
    Table that contains jokes and their associated fields.
    Related names: joke_ratings
    '''
    category = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    joke_source = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    joke_type = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    subject = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    joke_text = models.TextField(max_length=settings.TEXT_FIELD_MAX_LENGTH)
    joke_submitter = models.ForeignKey('JokeRater', null=True, blank=True, related_name='jokes_submitted')

    class Meta:
        db_table = 'Joke'

    def __str__(self):
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

    def get_rating_distribution(self):
        ''' Returns a list of how many ratings = 1,2,3,4,5 '''
        from api.models import JokeRating
        joke_ratings = JokeRating.objects.filter(joke=self)
        if joke_ratings.count():
            counts = [0, 0, 0, 0, 0]
            for jr in joke_ratings:
                counts[jr.rating-1] += 1
            return counts
        else:
            return [0, 0, 0, 0, 0]


class JokeRating(models.Model):
    '''
    Table that contains a JokeRating for an individual joke by an individual JokeRater.
    Related Names: jokes_submitted
    '''
    joke = models.ForeignKey('Joke', null=True, blank=True, related_name='joke_ratings')
    joke_rater = models.ForeignKey('JokeRater', null=True, blank=True, related_name='user_ratings')
    rating = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'JokeRating'

    def __str__(self):
        return "{0} | {1} | {2}".format(self.joke, self.joke_rater.joke_submitter_id, self.rating)


class JokeRater(models.Model):
    '''
    A user who went on Google Forms and filled out a form. Not the same as the user that logs in, although
    they are associated.

    TODO: create a relationship between this and a user account (optional).

    Related Names: user_ratings
    '''
    joke_submitter_id = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)

    gender = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    age = models.PositiveIntegerField()
    birth_country = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    major = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    preferred_joke_genre = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    preferred_joke_genre2 = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LENGTH)
    preferred_joke_type = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LENGTH)
    favorite_music_genre = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    favorite_movie_genre = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)

    class Meta:
        db_table = 'JokeRater'

    def __str__(self):
        return "JSMID: {0} | Age: {1} | Country: {2}".format(
                self.joke_submitter_id,
                self.age,
                self.birth_country
            )

        

# joke_categories = (
#     ('medicine', 'Medicine/Doctor'),
#     ('politics', 'Politics'),
#     ('programming', 'Programming'),
#     ('sports', 'Sports'),
#     ('children', 'Children'),
#     ('school', 'School'),
#     ('animal', 'Animal'),
#     ('lawyer', 'Lawyer'),
#     ('math', 'Math'),
#     ('nerd', 'Nerd'),
#     ('chuck_norris', 'Chuck Norris'),
#     ('dad', 'Dad')
# )


# joke_types = (
#     ('question', 'Question'),
#     ('pun', 'Pun'),
#     ('one-liner', 'One-Liner'),
#     ('dialogue', 'Dialogue'),
#     ('pickup_line', 'Pick Up Line'),
#     ('punch_line', 'Punch line'),
#     ('fun_fact', 'Fun Fact'),
#     ('other', 'Other')
# )


# joke_lengths = (
#     ('short', 'Short'),
#     ('medium', 'Medium'),
#     ('long', 'Long')
# )
