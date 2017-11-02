from django.contrib import admin

from .models import Joke, JokeRating, JokeRater

# Register your models here.
admin.site.register(Joke)
admin.site.register(JokeRating)
admin.site.register(JokeRater)