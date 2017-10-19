import random

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, JokeRatingForm
from api.models import Joke, JokeRating


@login_required
def show_joke(request):
    ''' '''
    available_jokes = Joke.objects.exclude(joke_ratings__user=request.user)

    # if user has rated all jokes, thank them for their service
    if not available_jokes:
        return render(request, 'jokerank/no-jokes-available.html', {})

    # get a random joke from the set of jokes they haven't rated
    joke = available_jokes[random.randint(0, available_jokes.count()-1)]

    # TODO: don't pass the joke to the user, they might change it
    # because they're mean
    context = {
        'joke': joke,
        'current_rating': joke.get_current_rating(),
        'joke_rating_form': JokeRatingForm(initial={
            'joke': joke, 'user': request.user})
    }
    return render(request, 'jokerank/jokes.html', context)


@login_required
def rate_joke(request):
    ''' '''
    if not request.method == 'POST':
        return HttpResponse('')
    form = JokeRatingForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['user'] != request.user:
            return HttpResponse('LIAR')
        form.save()
        return redirect(reverse('jokerank:show_joke'))
    else:
        return HttpResponse('Invalid form')


############################ AUTH VIEWS #################################

def signup(request):
    ''' View for creating a username/password/info. '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('jokerank:show_joke')
        else:
            return HttpResponse('')
    else:
        form = SignUpForm()
    return render(request, 'jokerank/signup.html', {'form': form})

def logout_success(request):
    return render(request, 'jokerank/logout-success.html')