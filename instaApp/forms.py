from django import forms
from .models import Comment, Profile, Image


class NewImagePost(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'image_name', 'image_caption']
        exclude = ['profile, user, Likes, comments, tags']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
        exclude = ['user']


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        exclude = ['image', 'profile', 'post_date']
