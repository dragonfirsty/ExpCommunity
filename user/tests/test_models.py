from django.test import TestCase
from user.models import User
from groups.models import Group

class UserTestModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_data = {
            "username":"shevchenko",
            "email":"shevchenko@mail.com",
            "first_name":"Andry",
            "last_name":"shevchenko",
            "birthdate":"1985-01-01",
            "password":"1234",
            "post_permission":True,
            "groups" : [{"name" :"geral1222"},{"name" : "geral1"}]
        }

        cls.user_data_2 = {
            "username":"shevchenkoo",
            "email":"shevchenkoo@mail.com",
            "first_name":"Andry",
            "last_name":"shevchenko",
            "birthdate":"1985-01-01",
            "password":"1234",
            "post_permission":True,
            "groups" : [{"name" :"geral1222"},{"name" : "geral1"}]
        }

        groups_data = cls.user_data.pop("groups")
        cls.user = User.objects.create(**cls.user_data)

        for value in groups_data:
            group, _ = Group.objects.get_or_create(**value)
            cls.user.groups.add(group) 

        groups_data_2 = cls.user_data_2.pop("groups")
        cls.user_2 = User.objects.create(**cls.user_data_2)
        for value in groups_data_2:
            group, _ = Group.objects.get_or_create(**value)
            cls.user_2.groups.add(group) 

    def test_user_fields(self):
        self.assertEqual(self.user.first_name, self.user_data['first_name'])
        self.assertEqual(self.user.last_name, self.user_data['last_name'])
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assert_(User._meta.get_field('first_name').max_length == 50)
        self.assert_(User._meta.get_field('last_name').max_length == 50)
        self.assert_(User._meta.get_field('email').unique == True)