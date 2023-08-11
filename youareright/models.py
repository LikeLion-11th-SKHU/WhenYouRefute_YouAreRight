from django.db import models

# Create your models here.


class Board(models.Model):
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
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    like_count = models.PositiveBigIntegerField(default=0)
    pub_date = models.DateTimeField()
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment


class Hashtag(models.Model):
    content = models.TextField(unique=True)
    count = models.PositiveBigIntegerField(default=1)
    hash_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content