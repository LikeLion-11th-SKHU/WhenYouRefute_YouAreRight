# Generated by Django 4.2.4 on 2023-08-18 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youareright', '0004_post_likes_alter_hashtag_hash_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='hash_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 8, 3, 2, 282453, tzinfo=datetime.timezone.utc)),
        ),
    ]
