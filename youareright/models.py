from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("data published")
    body = models.TextField()
    user_name = models.CharField(max_length=20, default="")
    count = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title
