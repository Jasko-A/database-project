from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.db.models import Avg

from .forms import SignUpForm, CreateJokeForm, EditJokeRaterForm
from api.models import Joke, JokeRating


@login_required
@require_http_methods(['GET'])
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def show_jokes(request):
    ''' 
    Page that shows the list of jokes, allows users to click on them
    and see their fields, etc.
    '''
    jokes = Joke.objects.annotate(avg_rating=Avg('joke_ratings__rating')).order_by('-avg_rating')

    prev_value = -1.0
    cur_ranking = 1
    num_repetitions = 1
    for joke in jokes:
        if joke.avg_rating == prev_value:
            joke.cur_ranking = cur_ranking
            print joke.avg_rating, joke.cur_ranking
            num_repetitions += 1
        else:
            joke.cur_ranking = cur_ranking
            print joke.avg_rating, joke.cur_ranking
            cur_ranking += num_repetitions
            num_repetitions = 1
            prev_value = joke.avg_rating


    context = {
        'jokes': jokes
    }
    return render(request, 'jokerank/jokes.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def add_joke(request):
    ''' 
    GET request means return the main add joke form page.
    POST request means try to create the joke they submitted, redirect if success.
    '''
    if request.method == 'GET':
        create_joke_form = CreateJokeForm()
        context = {
            'create_joke_form': create_joke_form
        }
        return render(request, 'jokerank/add-joke.html', context)
    else:
        create_joke_form = CreateJokeForm(request.POST)
        if create_joke_form.is_valid():
            create_joke_form.save(request.user.joke_rater)
            return redirect(reverse('jokerank:show_jokes'))
        else:
            context = {
                'create_joke_form': create_joke_form
            }
            return render(request, 'jokerank/add-joke.html', context)
        

@login_required
@require_http_methods(['GET'])
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def joke_details(request, joke_id):
    ''' 
    Render a page containing detials about the joke with ID=joke_id.
    '''
    try:
        joke = Joke.objects.get(id=joke_id)
        avg_rating = joke.get_current_rating()
        rating_distribution = joke.get_rating_distribution()
    except Exception as e:
        print "Error @joke_details: {0}.".format(e)
        return redirect(reverse('jokerank:show_jokes'))
    context = {
        'joke': joke,
        'joke_dist_x': [1, 2, 3, 4, 5],
        'joke_dist_y': rating_distribution
    }
    return render(request, 'jokerank/joke.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def user_profile(request):
    ''' 
    '''
    if request.method == 'GET':
        joke_rater = request.user.joke_rater
        joke_rater_form = EditJokeRaterForm(instance=joke_rater)
        context = {
            'joke_rater_form': joke_rater_form
        }
        return render(request, 'jokerank/user-profile.html', context)
    else:
        joke_rater = request.user.joke_rater
        joke_rater_form = EditJokeRaterForm(request.POST, instance=joke_rater)
        if joke_rater_form.is_valid():
            joke_rater_form.save()
            return redirect(reverse('stats:show_stats'))
        else:
            context = {
                'joke_rater_form': joke_rater_form
            }
            return render(request, 'jokerank/user-profile.html', context)



############################ AUTH VIEWS #################################


def signup(request):
    ''' 
    View for creating a username/password/info. 
    TODO: render errors if they input incorrectly.
    '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user, errors = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print errors
            for message in errors:
                print "messaging:", message
                messages.info(request, message)
            return redirect(reverse('user_profile'))
        else:
            context = {
                'form': form
            }
            return render(request, 'jokerank/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'jokerank/signup.html', {'form': form})


def logout_success(request):
    ''' 
    On logging out, user is redirected to this page. 
    '''
    return render(request, 'jokerank/logout-success.html')