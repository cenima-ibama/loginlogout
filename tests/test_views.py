from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.conf import settings

client = Client()
User = get_user_model()


class TestLoginLogoutView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('user', 'i@t.com', 'password')

    def test_loggin_response(self):
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_loggout_response(self):
        response = client.get(reverse('logout'))
        self.assertRedirects(response, reverse(settings.URL_AFTER_LOGIN))

    def login_and_logout(self):
        self.client.post(
            reverse('login'),
            {'username': self.user.username, 'password': 'password'}
        )
        self.assertIn('_auth_user_id', self.client.session)

        self.client.get(reverse('logout'))
        self.assertNotIn('_auth_user_id', self.client.session)
