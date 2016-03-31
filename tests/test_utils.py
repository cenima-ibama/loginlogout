from django.test import TestCase, Client

from django.conf import settings

from loginlogout.utils import *


class TestUtilsValidation(TestCase):

    def setUp(self):
        self.username = "user.name@example.br"

    def test_validation_util(self):
        validated = validate_user_funai(self.username, "@funai.local")
        self.assertEqual(validated, 'user.name@funai.local')

        self.username = "name.user@funai.gov.br"
        validated = validate_user_funai(self.username, "@funai.local")
        self.assertEqual(validated, 'name.user@funai.local')


        self.username = "name.user"
        validated = validate_user_funai(self.username, "@funai.local")
        self.assertEqual(validated, 'name.user@funai.local')

        self.username = "name.validate@validation.com"
        validated = validate_user_funai(self.username, "@funai.local")
        self.assertEqual(validated, 'name.validate@funai.local')





        