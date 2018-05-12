from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


'''
tags model class
'''


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


'''
Profile model class
'''


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    bio = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photos = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.user

    '''
    Class methods:
    find_profile: allows us to search for a user using their profile name.
    get_profile_by_id: allows us to get profile by id.
    '''
    @classmethod
    def find_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def get_profile_by_id(cls, user_id):
        profile = Profile.objects.get(id=user_id)
        return profile

'''
Image model class
'''


class Image(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True)
    image_name = models.CharField(max_length=60)
    image_caption = HTMLField()
    user = models.ForeignKey(User)
    likes = models.CharField(max_length=60)
    Comments = models.CharField(max_length=60)
    tags = models.ManyToManyField(Tag)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    '''
    Save an image to database.
    '''
    def save_image(self):
        self.save()

    '''
    Delete image from database.
    '''
    def delete_image(self):
        self.delete()

    '''
    Class method to Update image caption in database.
    '''
    @classmethod
    def update_caption(cls):
        pass

    '''
    Class method that Allows us to get a image using a its ID.
    '''
    @classmethod
    def get_image_by_id(cls, id):
        pass


'''
Comments model class
'''


class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image)
    profile = models.ForeignKey(User)
    post_date = models.DateTimeField(auto_now_add=True)
