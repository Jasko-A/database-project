from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from api.models import Joke, JokeRating, JokeRater


def show_stats(request):
    '''
    Home page of stats app, and therefore the whole site.

    Professor says (11/14): The minimum requirements for that are: number of jokes, number of users, distribution of each features. 
        The information should be dynamic (i.e. feeding from the DB) instead of static images. Look at high-charts and d3 solutions.
    '''
    # joke distribution stuff
    joke_category_x, joke_category_y = Joke.objects.category_distribution()
    joke_type_x, joke_type_y = Joke.objects.type_distribution()
    joke_source_x, joke_source_y = Joke.objects.source_distribution()

    # rating distribution stuff
    num_rating_category_x, num_rating_category_y = JokeRating.objects.num_ratings_joke_category_dist()
    num_rating_type_x, num_rating_type_y = JokeRating.objects.num_ratings_joke_type_dist()
    avg_rating_category_x, avg_rating_category_y = JokeRating.objects.avg_ratings_joke_category_dist()
    avg_rating_type_x, avg_rating_type_y = JokeRating.objects.avg_ratings_joke_type_dist()
    
    # rater distribution stuff
    preferred_joke_genre_x, preferred_joke_genre_y = JokeRater.objects.preferred_joke_genre_dist()
    preferred_joke_type_x, preferred_joke_type_y = JokeRater.objects.preferred_joke_type_dist()

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
    	'joke_source_y': joke_source_y,

      # ratings charts
      'num_rating_category_x': num_rating_category_x,
      'num_rating_category_y': num_rating_category_y,
      'num_rating_type_x': num_rating_type_x,
      'num_rating_type_y': num_rating_type_y,
      'avg_rating_category_x': avg_rating_category_x,
      'avg_rating_category_y': avg_rating_category_y,
      'avg_rating_type_x': avg_rating_type_x,
      'avg_rating_type_y': avg_rating_type_y,
      
      # rater charts
      'preferred_joke_genre_x': preferred_joke_genre_x,
      'preferred_joke_genre_y': preferred_joke_genre_y,
      'preferred_joke_type_x': preferred_joke_type_x,
      'preferred_joke_type_y': preferred_joke_type_y,
      
    }
    return render(request, 'stats/stats.html', context)


@login_required
@require_http_methods(['POST'])
def update_rating(request):
    ''' '''
    if not request.user.joke_rater:
        # print "no joke rater"
        return HttpResponse('')

    rating = request.POST.get('rating', None)
    if not rating:
        # print "invalid rating"
        return HttpResponse('')
    rating = int(rating)
    if rating > 5 or rating < 1:
        # print "invalid rating (not in range)"
        return HttpResponse('')

    try:
        joke = Joke.objects.get(id=request.POST.get('joke_id'))
    except:
        # print "joke not found"
        return HttpResponse('')

    try:
        joke_rating = JokeRating.objects.filter(joke_rater=request.user.joke_rater, joke=joke)
        if joke_rating.count() == 1:
            joke_rating = joke_rating[0]
            # print joke_rating.rating, "->", rating
            joke_rating.rating = rating
            joke_rating.save()
            # print "UPDATED RATING: {0}".format(joke_rating)
            return HttpResponse(True)
        elif joke_rating.count() == 0:
            jr = JokeRating.objects.create(rating=rating, joke_rater=request.user.joke_rater, joke=joke)
            # print "CREATED RATING: {0}".format(jr)
            return HttpResponse(True)
        else:
            # print "MULTIPLE OBJECTS RETURNED"
            return HttpResponse('')
    except Exception as e:
        print e
        return HttpResponse('')


