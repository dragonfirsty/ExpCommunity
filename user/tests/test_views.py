
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from user.models import User
from groups.models import Group


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
            "username":"shevchenkoo",
            "email":"shevchenkoo@mail.com",
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
	        "last_name" : "te",
	        "birthdate" : "1999-02-16",
	        
            }

        groups_data = cls.users_data_admin.pop("groups")
        users_admin = User.objects.create_superuser(**cls.users_data_admin)

        for value in groups_data:
            group, _ = Group.objects.get_or_create(**value)
            users_admin.groups.add(group)
        
        
        cls.users_admin_token = Token.objects.create(user = users_admin)
      
    def test_created_users(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.users_admin_token}")
        # import ipdb
        # ipdb.set_trace()
        response = self.client.post(self.base_url, data=self.users_data)
        print(response.data)
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)


















    # def test_login_with_valid_credentials(self):
    #     response = self.client.post(self.base_url_login, data=self.users_credentials)
    #         # print(response.data)
    #     self.assertEqual(status.HTTP_200_OK,response.status_code)
    
    # def test_token_fields_is_returned(self):
    #         response = self.client.post(self.base_url_login, data=self.users_credentials)
    #         # print(response.data)
    #         self.assertIn("token",response.data)    
        

    # def test_can_register_users_admin(self):
    #     response = self.client.post(self.base_url, data=self.users_data_admin)
    #     self.assertEqual(status.HTTP_201_CREATED,response.status_code)

    # def test_can_register_users(self):
    #     response = self.client.post(self.base_url, data=self.users_data)
    #     self.assertEqual(status.HTTP_401_UNAUTHORIZED,response.status_code)

    # def test_register_users_admin_fields(self):
    #     response = self.client.post(self.base_url, data=self.users_data_admin)
    #     expected_return_fields = ('uuid','username','email',"first_name","last_name",'birthdate','post_permission',"groups")

    #     self.assertEqual(len(response.data.keys()),8)

    #     for expected_field in expected_return_fields:
    #         self.assertIn(expected_field,response.data)

