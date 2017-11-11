from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def show_stats(request):
    '''
    Home page of stats app, and therefore the whole site.
    Render some plots? 
    Figure out how to do this dynamically (not just serving static .png/.jpg files)
    '''
    return render(request, 'stats/stats.html')
