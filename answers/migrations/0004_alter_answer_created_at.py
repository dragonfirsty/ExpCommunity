# Generated by Django 4.1 on 2022-09-13 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("answers", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
