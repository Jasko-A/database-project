from django import template
register = template.Library()

from api.models import JokeRater, Joke, JokeRating

@register.filter(name='user_joke_rating')
def user_joke_rating(joke, user):
	'''
	'''
	if not user.joke_rater:
		return -1

	joke_rater = user.joke_rater
	try:
		rating = JokeRating.objects.get(joke=joke, joke_rater=joke_rater)
	except Exception as e:
		print e
		return 0

	return rating.rating