from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model

from api.models import JokeRating, Joke, JokeRater
User = get_user_model()


class SignUpForm(UserCreationForm):
    ''' 
    Form for registering an account. 
    Only asks user for username, password, and password confirmation.
    Optionally allows them to link with their joke ratings they made.
    '''
    joke_submitter_id = forms.CharField(required=False, max_length=settings.CHAR_FIELD_MAX_LENGTH)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        '''
        On saving the model form, attempt to create a relationship between a JokeRater and
        this user (if they want to).
        '''
        user = super(SignUpForm, self).save(commit=False)

        if self.cleaned_data.get('joke_submitter_id'):
            try:
                joke_rater = JokeRater.objects.get(joke_submitter_id=self.cleaned_data.get('joke_submitter_id'))
                user.joke_rater = joke_rater
                user.save()
            except Exception as e:
                print "ERROR CREATING JOKE RATER -> JOKE USER RELATIONSHIP: {0}".format(e)

        if commit:
            user.save()
        return user



class CreateJokeForm(forms.ModelForm):
    ''' 
    A form for creating a joke.
    joke_source, joke_submitter automatically populated by user who created joke.
    '''
    class Meta:
        model = Joke
        fields = ('joke_text', 'category', 'joke_type', 'subject')