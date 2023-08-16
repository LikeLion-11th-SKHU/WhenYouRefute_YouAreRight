from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    SOCIETY = 'SO'
    CULTURE = 'CU'
    POLITICS = 'PO'
    ECONOMY = 'EC'
    ENTERTAINMENT = 'EN'
    FREE = 'FR'
    CATEGORY_CHOICES = (
        ('SOCIETY', '사회'),
        ('CULTURE', '문화'),
        ('POLITICS', '정치'),
        ('ECONOMY', '경제'),
        ('ENTERTAINMENT', '연예'),
        ('FREE', '자유'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='')
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("data published")
    body = models.TextField()
    user_name = models.CharField(max_length=20, default="")
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title
    

class Hashtag(models.Model):
    content = models.TextField(unique=True)
    count = models.PositiveBigIntegerField(default=1)
    hash_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.content
