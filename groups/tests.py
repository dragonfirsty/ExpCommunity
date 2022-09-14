from django.test import TestCase
from .models import Group

class GroupTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.group_1_data = {
            "name": "geral"
        }

        cls.group_1 = Group.objects.create(**cls.group_1_data)

    def test_group_fields(self):
        self.assertEqual(self.group_1.name, self.group_1_data["name"])
        self.assert_(Group._meta.get_field('name').max_length == 20)
        self.assert_(Group._meta.get_field('name').unique == True)