from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from api.models import Joke, JokeRating, JokeRater

# @login_required
def show_stats(request):
    '''
    Home page of stats app, and therefore the whole site.
    Render some plots? 
    Figure out how to do this dynamically (not just serving static .png/.jpg files)

    Professor says: The minimum requirements for that are: number of jokes, number of users, distribution of each features. 
        The information should be dynamic (i.e. feeding from the DB) instead of static images. Look at high-charts and d3 solutions.
    '''
    joke_category_x, joke_category_y = Joke.objects.category_distribution()
    joke_type_x, joke_type_y = Joke.objects.type_distribution()
    joke_source_x, joke_source_y = Joke.objects.source_distribution()

    context = {
    	'num_jokes': Joke.objects.count(),
    	'num_ratings': JokeRating.objects.count(),
    	'num_raters': JokeRater.objects.count(),

    	# joke charts
    	'joke_category_x': joke_category_x,
    	'joke_category_y': joke_category_y,
    	'joke_type_x': joke_type_x,
    	'joke_type_y': joke_type_y,
    	'joke_source_x': joke_source_x,
    	'joke_source_y': joke_source_y
    }
    return render(request, 'stats/stats.html', context)
