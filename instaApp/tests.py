from django.test import TestCase
from .models import Image, Comment, Profile, User


# Create your tests here.
class ImageTestClass(TestCase):
    '''
    Test case for the Image class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Image class
        '''
        # Create a image instance
        self.new_image = Image(caption='It blows')

    def test_instance(self):
        '''
        Test case to check if self.new_image in an instance of image class
        '''
        self.assertTrue(isinstance(self.new_image, Image))

    def test_get_photos(self):
        '''
        Test case to check if all images are retreived from the database
        '''
        found_photos = Image.get_photos()
        photos = Image.objects.all()

        self.assertTrue(len(found_photos) == len(photos))

    def test_get_profile_photos(self):
        '''
        Test case to check if all images for a specific profile are found from the database
        '''
        self.john = User(username="kiki")
        self.john.save()

        self.olive = User(username="ja-ne")
        self.olive.save()

        self.test_profile = Profile(user=self.olive, bio="Another Profile")
        self.test_image = Image(user=self.olive, caption="Another Profile")

        found_profile = Image.get_profile_images(self.olive.id)
        profiles = Image.objects.all()

        self.assertTrue(len(found_profile) == len(profiles))


class ProfileTestCase(TestCase):
    '''
    Test case for the Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of Profile class
        self.new_profile = Profile(bio="I am Groot")

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_get_profiles(self):
        '''
        Test case to check if all profiles are retreived from the database
        '''
        found_profiles = Profile.get_profiles()
        profiles = Profile.objects.all()

        self.assertTrue(len(found_profiles) == len(profiles))


class CommentTestCase(TestCase):
    '''
    Test case for the Comment class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comment(comment='Hit th fan')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_get_image_comments(self):
        '''
        Test case to check if get image comments is getting comments for a specific image
        '''
        self.john = User(username="shem")
        self.john.save()

        self.olive = User(username="ppole")
        self.olive.save()

        self.test_profile = Profile(user=self.olive, bio="Another Profile")
        self.test_image = Image(user=self.olive, caption="Another Profile")

        self.test_comment = Comment(image=self.test_image, comment="how could you?")

        found_comments = Comment.get_image_comments(self.test_image.id)

        comments = Comment.objects.all()

        # No comments were saved so expect True
        self.assertTrue(len(found_comments) == len(comments))
