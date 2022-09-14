
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from user.models import User
from groups.models import Group
from django.urls import reverse


class UserViewsTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
       
        cls.base_url = '/api/users/'

        cls.base_url_login = '/api/users/login/'

        

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
            "groups" : [{"name" :"geral1222"},{"name" : "geral1"}]
        }

        

        cls.users_data = {
	        "username" : "testando",
	        "email" : "testando@email.com",
	        "password": "ronaldinho12",
            "groups" : [{"name" :"geral1222"},{"name" : "geral1"}],
	        "first_name" : "tes",
	        "last_name" : 5,
	        "birthdate" : "1999-02-16",
	        "groups" : [{"name" :"geral1222"},{"name" : "geral1"}]
            }

            

        groups_data = cls.users_data_admin.pop("groups")
        users_admin = User.objects.create_superuser(**cls.users_data_admin)

        for value in groups_data:
            group, _ = Group.objects.get_or_create(**value)
            users_admin.groups.add(group)
        
        cls.users_admin_token = Token.objects.create(user = users_admin)

        cls.base_url_detail = reverse("users-detail", kwargs={"pk":users_admin.uuid})
        

    def test_created_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        response = self.client.post(self.base_url, data=self.users_data)
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)

    def test_unauthenticated_created_users(self):
        response = self.client.post(self.base_url, data=self.users_data)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_login_with_valid_credentials(self):
        response = self.client.post(self.base_url_login, data=self.users_credentials)
        self.assertEqual(status.HTTP_200_OK,response.status_code)
    
    def test_token_fields_is_returned(self):
        response = self.client.post(self.base_url_login, data=self.users_credentials)
        self.assertIn("token",response.data)    

    def test_list_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        response = self.client.get(self.base_url)
        self.assertEqual(status.HTTP_200_OK,response.status_code)

    def test_unauthenticated_list_users(self):
        response = self.client.get(self.base_url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_update_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        response = self.client.patch(self.base_url_detail, data={"first_name" : "Adriano"})
        self.assertEqual(status.HTTP_200_OK,response.status_code)

    def test_unauthenticated_update_users(self):
        response = self.client.patch(self.base_url_detail, data={"first_name" : "Adriano"})
        self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)

    def test_delete_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        response = self.client.delete(self.base_url_detail)
        self.assertEqual(status.HTTP_204_NO_CONTENT,response.status_code)

    def test_unauthenticated_delete_users(self):
        response = self.client.delete(self.base_url_detail)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)