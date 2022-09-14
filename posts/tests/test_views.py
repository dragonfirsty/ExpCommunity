from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from user.models import User
from groups.models import Group
from django.urls import reverse
from posts.models import Post

class GroupViewsTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
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

        cls.posts_data_create = {
            "description" : "Testando galera",
	        "media" : "HAHAHAHAHAHAHAHAHAHAHA To codando"
        }

        groups_data = cls.users_data_admin.pop("groups")
        users_admin = User.objects.create_superuser(**cls.users_data_admin)
        group_uuid = ""
        for value in groups_data:
            group, _ = Group.objects.get_or_create(**value)
            users_admin.groups.add(group)
            group_uuid = group.uuid
        
        cls.users_admin_token = Token.objects.create(user = users_admin)
        cls.base_url = reverse("groups", kwargs={"group_id":group_uuid})

        
        

    def test_created_posts(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        response = self.client.post(self.base_url, data=self.posts_data_create)
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)

    def test_unauthenticated_created_posts(self):
        response = self.client.post(self.base_url, data=self.posts_data_create)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)  

    def test_list_posts(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        response = self.client.get(self.base_url)
        self.assertEqual(status.HTTP_200_OK,response.status_code)

    def test_unauthenticated_list_posts(self):
        response = self.client.get(self.base_url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)

    
    

