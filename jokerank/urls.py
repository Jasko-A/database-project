from django.conf.urls import url

from . import views

app_name = 'jokerank'
urlpatterns = [
    url(r'^$', views.show_jokes, name='show_jokes'),
]