# Generated by Django 4.1.1 on 2022-09-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_created_at_alter_user_update_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=40),
        ),
    ]
