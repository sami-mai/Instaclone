from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.dispatch import receiver


class WelcomeEmailRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()


class Tag(models.Model):
    '''
    Tag nodel class that defines categories of posts and tags on posts
    '''
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    @classmethod
    def get_tags(cls):
        tags = Tag.objects.all()
        return tags


class Profile(models.Model):
    '''
    Profile model class
    '''
    avatar = models.ImageField(upload_to='avatar/', blank=True)
    bio = HTMLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # Create Profile when creating a User
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # Save Profile when saving a User
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    '''
    Class methods:
    update_profile:
    find_profile: allows us to search for a user using their profile name.
    get_profile_by_id: allows us to get profile by id.
    '''
    @classmethod
    def update_profile(cls, id, bio):
        update = Image.objects.filter(id=id).update(bio=bio)
        return update

    @classmethod
    def find_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def get_profiles(cls):
        profiles = Profile.objects.all()
        return profiles


class Image(models.Model):
    '''
    Image model class
    '''
    image = models.ImageField(upload_to='photos/', blank=True)
    image_name = models.CharField(max_length=60)
    image_caption = HTMLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    likes = models.CharField(max_length=60)
    tags = models.ManyToManyField(Tag)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['post_date']

    def save_image(self):
        self.save()

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
    def get_photo_by_id(cls, id):
        pass

    @classmethod
    def get_photos(cls):

        photos = Image.objects.all()

        return photos

    @classmethod
    def get_profile_photos(cls, profile_id):
        profile_images = Image.objects.filter(profile=profile_id).all()
        return profile_images


class Comment(models.Model):
    '''
    Comments model class
    '''
    comment = models.TextField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_comments(cls, image_id):
        comments = Comment.objects.filter(image=image_id)
        return comments
