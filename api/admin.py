from django.contrib import admin

from .models import Joke, JokeRating, JokeRater

admin.site.register(Joke)
admin.site.register(JokeRating)
admin.site.register(JokeRater)