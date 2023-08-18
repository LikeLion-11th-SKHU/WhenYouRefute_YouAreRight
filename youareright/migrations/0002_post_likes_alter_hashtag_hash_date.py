# Generated by Django 4.2.4 on 2023-08-18 12:32

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('youareright', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='hash_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 12, 32, 8, 951021, tzinfo=datetime.timezone.utc)),
        ),
    ]
