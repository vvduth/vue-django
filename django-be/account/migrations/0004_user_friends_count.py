# Generated by Django 5.2.1 on 2025-05-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_user_friends_friendshiprequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="friends_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
