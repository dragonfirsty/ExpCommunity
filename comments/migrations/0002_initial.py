# Generated by Django 4.1 on 2022-09-13 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("comments", "0001_initial"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_post",
                to="posts.post",
            ),
        ),
    ]
