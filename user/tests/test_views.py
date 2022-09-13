from django.test import TestCase
from rest_framework.views import status

from user.models import User

class UserRegisterViewTest(TestCase):
    
    @classmethod

    def setUpTestData(cls) -> None:
        cls.base_url = '/api/users/'
        cls.users_data_admin = {
            "username":"shevchenko",
            "email":"shevchenko@mail.com",
            "first_name":"Andry",
            "last_name":"shevchenko",
            "birthdate":"1985-01-01",
            "password":"1234",
            "post_permission":True,
            "is_superuser":True

        }

        cls.users_data = {
            "username":"leonelmessi",
            "email":"messi@mail.com",
            "first_name":"Leonel",
            "last_name":"Messi",
            "birthdate":"1985-01-01",
            "password":"1234",
            "post_permission":True,
            "is_superuser":False

        }
    

    def test_can_register_users_admin(self):
        response = self.client.post(self.base_url, data=self.users_data_admin)

        self.assertEqual(status.HTTP_201_CREATED,response.status_code)


    def test_register_users_admin_fields(self):
        response = self.client.post(self.base_url, data=self.users_data_admin)
        expected_return_fields = ("id","username","email","first_name","last_name","birthdate","post_permission","is_superuser")

        self.assertEqual(len(response.data.keys()),8)

        for expected_field in expected_return_fields:
            self.assertIn(expected_field,response.data)


    class LoginTest(TestCase):
        @classmethod
        def setUpTestData(cls) -> None:
            cls.base_url = '/api/users/'
            cls.users_credentials = {
            "username":"shevchenko",
            "password":"1234"
        }
            cls.users_data_admin = {
            "username":"shevchenko",
            "email":"shevchenko@mail.com",
            "first_name":"Andry",
            "last_name":"shevchenko",
            "birthdate":"1985-01-01",
            "password":"1234",
            "post_permission":True,
            "is_superuser":True

        }

            cls.users = User.objects.create_user(**cls.users_data_admin)

        def test_login_with_valid_credentials(self):
            response = self.client.post(self.base_url, data=self.users_credentials)
            self.assertEqual(status.HTTP_200_OK,response.status_code)

        def test_token_fields_is_returned(self):
            response = self.client.post(self.base_url, data=self.users_credentials)
            self.assertIn("token",response.data)