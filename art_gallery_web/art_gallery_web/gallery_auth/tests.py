from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client

from django.urls import reverse

from art_gallery_web.gallery_app.models import Arts


class ProfileModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create()

    def test_profile(self):
        userprofile = get_user_model().objects.last().userprofile


UserModel = get_user_model()


class ArtTestCase(TestCase):
    logged_in_user_username = 'nedkorachev'
    logged_in_user_email = 'nedko@rachev.it'
    logged_in_user_password = '12345qwe'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
            username=self.logged_in_user_username,
        )


class ProfileDetailsTest(ArtTestCase):
    def test_getDetails_whenLoggedInUserWithNoArts_shouldGetDetailsWithNoArts(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('my_profile'))

        self.assertListEmpty(list(response.context['arts']))

    def test_getDetails_whenLoggedInUserWithArts_shouldGetDetailsWithArts(self):
        art = Arts.objects.create(
            name='Test Art',
            height=10,
            width=20,
            price=120,
            description='TEst art description',
            image='path/to/image.png',

            created_by=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('my_profile'))

        self.assertEqual(200, response.status_code)

        self.assertListEqual([art], list(response.context['arts']))


class LoginTest(ArtTestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test1234', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='test1234')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='test1234')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
