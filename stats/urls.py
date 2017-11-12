from django.conf.urls import url

from . import views

app_name = 'stats'
urlpatterns = [
    url(r'^$', views.show_stats, name='show_stats'),
    url(r'^rating/update/$', views.update_rating, name='update_rating'),

]