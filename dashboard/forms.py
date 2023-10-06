from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from ckeditor.widgets import CKEditorWidget

from .models import DiscussionPost, DiscussionComment

class RegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {
                'class': 'username',
                'placeholder': 'Username',
                'id': 'username',
                'name': 'username',
                'type': 'text'
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'class': 'email',
                'placeholder': 'Email',
                'id': 'email',
                'name': 'email',
                'type': 'email'
            }
        )

        self.fields['password1'].widget.attrs.update(
            {
                'class': 'password1',
                'placeholder': 'Password',
                'id': 'password1',
                'name': 'password1',
                'type': 'password'
            }
        )

        self.fields['password2'].widget.attrs.update(
            {
                'class': 'password2',
                'placeholder': 'Confirm Password',
                'id': 'password2',
                'name': 'password2',
                'type': 'password'
            }
        )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class CreateDiscussionPostForm(ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = DiscussionPost
        fields = ['title', 'description']

class CreateDiscussionCommentForm(ModelForm):
    commentBody = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = DiscussionComment
        fields = ['commentBody']