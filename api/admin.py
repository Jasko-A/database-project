from django.contrib import admin

from .models import Joke, JokeRating, JokeRater

# register all models to the admin page.
admin.site.register(Joke)
admin.site.register(JokeRating)
admin.site.register(JokeRater)