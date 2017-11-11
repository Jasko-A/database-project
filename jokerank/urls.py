from django.conf.urls import url

from . import views

app_name = 'jokerank'
urlpatterns = [
    url(r'^$', views.show_jokes, name='show_jokes'),
    url(r'^add/$', views.add_joke, name='add_joke'),
    url(r'^details/(?P<joke_id>[0-9]+)/$', views.joke_details, name='joke_details'),
]