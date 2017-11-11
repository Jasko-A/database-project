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
        ''' '''
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

    def clean_joke_submitter_id(self):
        '''
        Check if the joke_submitter_id actually points to a joke rater.
        '''
        cleaned_data = self.cleaned_data
        if 'joke_submitter_id' in cleaned_data.keys():
            jsmid = cleaned_data.get('joke_submitter_id')
            if not jsmid: return
            try:
                jsm = JokeRater.objects.get(joke_submitter_id=jsmid)
            except JokeRater.DoesNotExist:
                raise forms.ValidationError('There is no Joke Rater with id = {0}. Send us an email if you think this is wrong.'.format(jsmid))
            except JokeRater.MultipleObjectsReturned:
                raise forms.ValidationError('There are multiple JokeRaters with the same ID = {0}.'.format(
                    jsmid))
            except Exception as e:
                raise forms.ValidationError(e)
        return cleaned_data.get('joke_submitter_id')

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
        widgets = {
            'category': forms.Select(choices=JOKE_CATEGORIES),
            'joke_type': forms.Select(choices=JOKE_TYPES)
        }

    def __init__(self, *args, **kwargs):
        ''' '''
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

        # update the submitter
        joke.joke_source = 'website'
        joke.joke_submitter = joke_submitter

        if commit:
            joke.save()
        return joke


