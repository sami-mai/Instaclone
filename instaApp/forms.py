from django import forms
from .models import Comment, Profile, Image, User


class WelcomeEmailForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_name', 'image_caption']
        exclude = ['profile, user, Likes, comments, tags']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        exclude = ['user']


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        # exclude = ['image', 'profile', 'post_date']
