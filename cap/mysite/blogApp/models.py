from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    signature = models.CharField(max_length=50, default="keep on rocking")
    date = models.DateTimeField()


def __str__(self):
    return self.title
