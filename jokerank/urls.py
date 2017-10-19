from django.conf.urls import url

from . import views

app_name = 'jokerank'
urlpatterns = [
    url(r'^$', views.show_joke, name='show_joke'),
    url(r'^rate/$', views.rate_joke, name='rate_joke'),
]