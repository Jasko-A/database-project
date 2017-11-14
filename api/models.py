from django.db import models
from django.conf import settings
from django.db.models import Avg


JOKE_CATEGORIES = (
    ('Medicine/Doctor', 'Medicine/Doctor'),
    ('Politics', 'Politics'),
    ('Programming', 'Programming'),
    ('Sports', 'Sports'),
    ('Children', 'Children'),
    ('School', 'School'),
    ('Animal', 'Animal'),
    ('Lawyer', 'Lawyer'),
    ('Math', 'Math'),
    ('Nerd', 'Nerd'),
    ('Chuck Norris', 'Chuck Norris'),
    ('Dad', 'Dad'),
    ('Other', 'Other')
)

JOKE_TYPES = (
    ('Question', 'Question'),
    ('Pun', 'Pun'),
    ('One-liner', 'One-liner'),
    ('Dialogue', 'Dialogue'),
    ('Pick Up Line', 'Pick Up Line'),
    ('Punch line', 'Punch line'),
    ('Fun Fact', 'Fun Fact'),
    ('Story', 'Story'),
    ('Other', 'Other')
)


class JokeManager(models.Manager):
    ''' '''
    def category_distribution(self):
        ''' returns [categories], [counts] '''
        categories = [t[1] for t in JOKE_CATEGORIES]
        counts = []
        for category in categories:
            counts.append(self.filter(category=category).count())
        return categories, counts

    def type_distribution(self):
        ''' returns [types], [counts] '''
        types = [t[1] for t in JOKE_TYPES]
        counts = []
        for joke_type in types:
            counts.append(self.filter(joke_type=joke_type).count())
        types.append('None')
        counts.append(self.filter(joke_type='').count())
        return types, counts

    def source_distribution(self):
        ''' '''
        all_sources = ['Class', 'Data Team', 'Website']
        counts = []
        counts.append(self.filter(joke_source__startswith='C').count())
        counts.append(self.filter(joke_source__startswith='D').count())
        counts.append(self.filter(joke_source__startswith='W').count())
        return all_sources, counts

class Joke(models.Model):
    '''
    Table that contains jokes and their associated fields.
    Related names: joke_ratings
    '''
    objects = JokeManager()

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
            return -1

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



class JokeRatingManager(models.Manager):
    ''' 
    Subclassed manager for the JokeRating Model. 
    Supplies class-wide methods (kind of like static methods, apply to entire JokeRating table in the db)
    '''
    def avg_ratings_joke_type_dist(self):
        ''' Returns [types], [ratings] '''
        ratings = []
        types = [t[1] for t in JOKE_TYPES]
        for joke_type in types:
            avg_rating = self.filter(
                    joke__joke_type=joke_type
                ).aggregate(Avg('rating'))
            ratings.append(avg_rating['rating__avg'])
        return types, ratings

    def avg_ratings_joke_category_dist(self):
        ''' '''
        ratings = []
        categories = [t[1] for t in JOKE_CATEGORIES]
        for category in categories:
            avg_rating = self.filter(
                    joke__category=category
                ).aggregate(Avg('rating'))
            ratings.append(avg_rating['rating__avg'])
        return categories, ratings

    def num_ratings_joke_type_dist(self):
        ''' '''
        counts = []
        types = [t[1] for t in JOKE_TYPES]
        for joke_type in types:
            num_ratings = self.filter(joke__joke_type=joke_type).count()
            counts.append(num_ratings)
        return types, counts

    def num_ratings_joke_category_dist(self):
        ''' '''
        counts = []
        categories = [t[1] for t in JOKE_CATEGORIES]
        for category in categories:
            num_ratings = self.filter(joke__category=category).count()
            counts.append(num_ratings)
        return categories, counts

class JokeRating(models.Model):
    '''
    Table that contains a JokeRating for an individual joke by an individual JokeRater.
    Related Names: jokes_submitted
    '''
    objects = JokeRatingManager()
    joke = models.ForeignKey('Joke', null=True, blank=True, related_name='joke_ratings')
    joke_rater = models.ForeignKey('JokeRater', null=True, blank=True, related_name='user_ratings')
    rating = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'JokeRating'

    def __str__(self):
        return "{0} | {1} | {2}".format(self.joke, self.joke_rater.joke_submitter_id, self.rating)


class JokeRaterManager(models.Manager):
    ''' '''
    def preferred_joke_genre_dist(self):
        ''' '''
        counts = []
        genres = [t[1] for t in JOKE_CATEGORIES]
        for genre in genres:
            counts.append(self.filter(preferred_joke_genre=genre).count())
        return genres, counts
    
    def preferred_joke_type_dist(self):
        ''' '''
        counts = []
        types = [t[1] for t in JOKE_TYPES]
        for joke_type in types:
            counts.append(self.filter(preferred_joke_type=joke_type).count())
        return types, counts

class JokeRater(models.Model):
    '''
    A user who went on Google Forms and filled out a form. Not the same as the user that logs in, although
    they are associated.

    TODO: create a relationship between this and a user account (optional).

    Related Names: user_ratings
    '''
    objects = JokeRaterManager()
    joke_submitter_id = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)

    gender = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    age = models.PositiveIntegerField(null=True)
    birth_country = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LENGTH)
    major = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    preferred_joke_genre = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    preferred_joke_genre2 = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    preferred_joke_type = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    favorite_music_genre = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)
    favorite_movie_genre = models.CharField(max_length=settings.CHAR_FIELD_MAX_LENGTH)

    class Meta:
        db_table = 'JokeRater'

    def __str__(self):
        return "JSMID: {0} | Age: {1} | Country: {2}".format(
                self.joke_submitter_id,
                self.age,
                self.birth_country)
