from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    like_count = models.PositiveBigIntegerField(default=0)
    pub_date = models.DateTimeField()
    File = models.FileField(upload_to="files/", null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    hit = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title


class Reply(models.Model):
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment
