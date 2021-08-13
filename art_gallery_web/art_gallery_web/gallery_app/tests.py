import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import TestCase, Client

from django.urls import reverse

from art_gallery_web.gallery_app.models import is_negative, Arts, Post


# test custom validator in Arts_Model
class ValidateIsNegativeTests(TestCase):
    def test_whenValueIsGreaterThanZero_expectToDoNothing(self):
        value = 5
        is_negative(value)

    def test_whenValueIsZero_expectToRaise(self):
        value = 0
        with self.assertRaises(ValidationError) as message:
            is_negative(value)
        self.assertIsNotNone(message.exception)

    def test_whenValueIsLessThanZero_expectToRaise(self):
        value = -3
        with self.assertRaises(ValidationError) as message:
            is_negative(value)
        self.assertIsNotNone(message.exception)


# test model Arts
class ArtModelTest(TestCase):
    def test_whenHeightWeightPriceIsZero_expectToRaise(self):
        name = 'Test1'
        height = 0
        width = 0
        price = 0
        description = 'The test1'
        mock_image = SimpleUploadedFile(name='test_image1.jpg', content=b'', content_type='image/jpeg')
        user = User.objects.create(username='Test1', password='test1123456')
        test_art = Arts(name=name, height=height, width=width, price=price, description=description, image=mock_image,
                        created_by=user)

        with self.assertRaises(ValidationError) as message:
            test_art.full_clean()
            test_art.save()
        self.assertIsNotNone(message.exception)

    def test_whenPriceIsLessZero_expectToRaise(self):
        name = 'Test2'
        height = 30
        width = 50
        price = -30
        description = 'The test2'
        mock_image = SimpleUploadedFile(name='test_image2.jpg', content=b'', content_type='image/jpeg')
        user = User.objects.create(username='Test2', password='test2123456')
        test_art = Arts(name=name, height=height, width=width, price=price, description=description, image=mock_image,
                        created_by=user)

        with self.assertRaises(ValidationError) as message:
            test_art.full_clean()
            test_art.save()
        self.assertIsNotNone(message.exception)

    def test_whenHeightWeightPriceIsPositive_expectSuccess(self):
        name = 'Test3'
        height = 30
        width = 50
        price = 130
        description = 'The test2 '
        mock_image = SimpleUploadedFile(name='test_image3.jpg', content=b'', content_type='image/jpeg')
        user = User.objects.create(username='Test3', password='test2123456')
        test_art = Arts(name=name, height=height, width=width, price=price, description=description, image=mock_image,
                        created_by=user)

        test_art.full_clean()
        test_art.save()


# test model Post
class PostModelTest(TestCase):
    # mock art
    def test_PostModel_expectSuccess(self):
        name = '1'
        height = 30
        width = 50
        price = 130
        description = '1'
        mock_image = SimpleUploadedFile(name='test_image_post.jpg', content=b'', content_type='image/jpeg')
        user = User.objects.create(username='Post', password='postpost123')
        test_art_post = Arts(name=name, height=height, width=width, price=price, description=description,
                             image=mock_image,
                             created_by=user)
        test_art_post.full_clean()
        test_art_post.save()
        # mock post
        text = 'Hello'
        name_post = 'Test_Name'
        email = 'test@gmail.com'
        created_on = datetime.datetime(2008, 5, 5, 16, 20)
        test_post = Post(text=text, created_on=created_on, name=name_post, email=email, art=test_art_post)

        test_post.full_clean()
        test_post.save()


# test indexView
class IndexViewTests(TestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')


# test aboutView
class AboutViewTests(TestCase):
    def test_about(self):
        client = Client()
        response = client.get(reverse('about page'))
        self.assertTemplateUsed(response, 'about.html')


# test listView
class ListViewTests(TestCase):
    def test_about(self):
        client = Client()
        response = client.get(reverse('list arts'))
        self.assertTemplateUsed(response, 'arts/arts_list.html')
