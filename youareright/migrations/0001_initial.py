# Generated by Django 4.2.4 on 2023-08-16 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
                ('count', models.PositiveBigIntegerField(default=1)),
                ('hash_date', models.DateTimeField(default=datetime.datetime(2023, 8, 16, 21, 54, 18, 298934, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SOCIETY', '사회'), ('CULTURE', '문화'), ('POLITICS', '정치'), ('ECONOMY', '경제'), ('ENTERTAINMENT', '연예'), ('FREE', '자유')], default='', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
                ('body', models.TextField()),
                ('user_name', models.CharField(default='', max_length=20)),
                ('count', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('hashtags', models.ManyToManyField(blank=True, to='youareright.hashtag')),
            ],
        ),
    ]
