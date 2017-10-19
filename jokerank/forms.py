from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model

from api.models import JokeRating
User = get_user_model()


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'gender', )


class JokeRatingForm(forms.ModelForm):

    class Meta:
        model = JokeRating
        fields = ('rating', 'would_recommend', 'joke', 'user')
        widgets = {
            'joke': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }
