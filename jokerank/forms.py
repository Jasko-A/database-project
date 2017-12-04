from iso3166 import countries

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import get_user_model

from api.models import JokeRating, Joke, JokeRater, JOKE_CATEGORIES, JOKE_TYPES
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

    def __init__(self, *args, **kwargs):
        ''' 
        Initialize the widgets of the form (add the Bootstrap class form-control, placeholders).
        '''
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'placeholder': 'Username',
            'class': 'form-control'
        }
        self.fields['password1'].widget.attrs = {
            'placeholder': 'Password',
            'class': 'form-control'
        }
        self.fields['password2'].widget.attrs = {
            'placeholder': 'Password Again',
            'class': 'form-control'
        }
        self.fields['joke_submitter_id'].widget.attrs = {
            'placeholder': 'Joke Submitter ID (optional)',
            'class': 'form-control'
        }

    def save(self, commit=True):
        '''
        On saving the model form, attempt to create a relationship between a JokeRater and
        this user (if they want to).
        '''
        errors = []
        user = super(SignUpForm, self).save(commit=False)
        jsmid = self.cleaned_data.get('joke_submitter_id')
        if jsmid:
            try:
                joke_rater = JokeRater.objects.get(
                    joke_submitter_id=self.cleaned_data.get('joke_submitter_id'))
            except JokeRater.DoesNotExist: # no joke rater in DB with that ID
                joke_rater = JokeRater.objects.create(joke_submitter_id=jsmid)
                errors.append('There was no Joke Rater with ID={0}. We created one for you.'.format(jsmid))
            except JokeRater.MultipleObjectsReturned: # multiple joke raters with that ID
                errors.append('Database Corruption. There were multiple JokeRaters with the same ID={0}.'.format(jsmid))
                errors.append('Creating a new joke rater for you to use.')
                joke_rater = JokeRater.objects.create()

            # already associated with someone
            if hasattr(joke_rater, 'user'):
                errors.append('That joke submitter id is already associated with a user. We created a new one for you.')
                joke_rater = JokeRater.objects.create()
        else:
            joke_rater = JokeRater.objects.create()
            
        user.joke_rater = joke_rater

        if commit:
            user.save()
        return user, errors


class CreateJokeForm(forms.ModelForm):
    ''' 
    A form for creating a joke.
    joke_source, joke_submitter automatically populated by user who created joke.
    '''
    class Meta:
        model = Joke
        fields = ('joke_text', 'category', 'joke_type', 'subject')
        widgets = {
            'category': forms.Select(choices=JOKE_CATEGORIES),
            'joke_type': forms.Select(choices=JOKE_TYPES)
        }

    def __init__(self, *args, **kwargs):
        ''' 
        Initialize the widgets of the form (add the Bootstrap class form-control, placeholders).
        '''
        super(CreateJokeForm, self).__init__(*args, **kwargs)
        self.fields['joke_text'].widget.attrs = {
            'placeholder': 'The joke itself.',
            'class': 'form-control'
        }
        self.fields['category'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['joke_type'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['subject'].widget.attrs = {
            'placeholder': 'Joke Subject (e.g. Donald Trump)',
            'class': 'form-control'
        }

    def save(self, joke_submitter, commit=True):
        '''
        On saving the model form, auto fill the joke_source and joke_submitter.
        '''
        joke = super(CreateJokeForm, self).save(commit=False)
        joke.joke_source = 'website'
        joke.joke_submitter = joke_submitter
        if commit:
            joke.save()
        return joke


AGES = tuple([(i, i) for i in range(1, 100)])
GENDER = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Prefer not to say', 'Prefer not to say'),
)
COUNTRIES = tuple([(c.name, c.name) for c in countries])
MAJOR = (
    ('Computer Science/CSE', 'Computer Science/CSE'),
    ('Physics', 'Physics'),
    ('Math', 'Math'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Biochemical Engineering', 'Biochemical Engineering'),
    ('Other', 'Other')
)
MUSIC = (
    ('Rock', 'Rock'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Rap', 'Rap'),
    ('Metal', 'Metal'),
    ('Pop', 'Pop'),
    ('Jazz', 'Jazz'),
    ('Blues', 'Blues'),
    ('Country', 'Country'),
    ('Alternative Rock', 'Alternative Rock'),
    ('Indie', 'Indie'),
    ('Reggae', 'Reggae'),
    ('Classical', 'Classical'),
    ('EDM', 'EDM')
)
MOVIES = (
    ('Thriller', 'Thriller'),
    ('Horror', 'Horror'),
    ('Action', 'Action'),
    ('Superhero', 'Superhero'),
    ('Mystery', 'Mystery'),
    ('Comedy', 'Comedy'),
    ('Romantic comedy', 'Romantic comedy'),
    ('SciFi', 'SciFi'),
    ('Documentary', 'Documentary'),
    ('Indie', 'Indie'),
    ('Family', 'Family')
)

class EditJokeRaterForm(forms.ModelForm):
    '''
    Form for editing your user account after it is created.
    '''
    class Meta:
        model = JokeRater
        exclude = ('joke_submitter_id', 'id')
        widgets = {
            'age': forms.Select(choices=AGES),
            'gender': forms.Select(choices=GENDER),
            'birth_country': forms.Select(choices=COUNTRIES),
            'major': forms.Select(choices=MAJOR),
            'preferred_joke_genre': forms.Select(choices=JOKE_CATEGORIES),
            'preferred_joke_genre2': forms.Select(choices=JOKE_CATEGORIES),
            'preferred_joke_type': forms.Select(choices=JOKE_TYPES),
            'favorite_music_genre': forms.Select(choices=MUSIC),
            'favorite_movie_genre': forms.Select(choices=MOVIES),
        }

    def __init__(self, *args, **kwargs):
        ''' 
        Initialize the widgets of the form (add the Bootstrap class form-control, placeholders).
        '''
        super(EditJokeRaterForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['age'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['birth_country'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['major'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['preferred_joke_genre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['preferred_joke_genre2'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['preferred_joke_type'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['favorite_music_genre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['favorite_movie_genre'].widget.attrs = {
            'class': 'form-control'
        }

