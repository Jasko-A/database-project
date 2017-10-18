from django.contrib import admin

from .models import Joke, JokeRating

# Register your models here.
admin.site.register(Joke)
admin.site.register(JokeRating)