from django import template
register = template.Library()

from api.models import JokeRater, Joke, JokeRating


@register.filter(name='user_joke_rating')
def user_joke_rating(joke, user):
	'''
	Django template filter for checking the rating the user gave each joke in the page.
	Returns: rating || 0 if not rated || -1 if no associated joke rater
	'''
	if not user.joke_rater: return -1

	joke_rater = user.joke_rater

	# user has not yet rated the joke
	try:
		rating = JokeRating.objects.get(joke=joke, joke_rater=joke_rater)
	except Exception as e:
		return 0

	return rating.rating