# Generated by Django 4.2.4 on 2023-08-18 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youareright', '0005_alter_hashtag_hash_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='hash_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 18, 11, 7, 18, 51634, tzinfo=datetime.timezone.utc)),
        ),
    ]
