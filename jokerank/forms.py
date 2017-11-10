from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model

from api.models import JokeRating
User = get_user_model()


class SignUpForm(UserCreationForm):
    ''' 
    Form for registering an account. 
    Only asks user for username, password, and password confirmation.
    
    TODO: update this to make a tie between a user and the jokeratings they have already made
        that are saved under JokeRater model.
    '''
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


# TODO: add a CreateJokeForm


# class JokeRatingForm(forms.ModelForm):

#     class Meta:
#         model = JokeRating
#         fields = ('rating', 'joke', 'joke_rater')
#         widgets = {
#             'joke': forms.HiddenInput(),
#             'user': forms.HiddenInput()
#         }
