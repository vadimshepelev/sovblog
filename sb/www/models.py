from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    datetime = models.DateTimeField(u'Дата публикации')
    content = models.TextField(max_length=10000)
    image = models.CharField(max_length=256)

    def __str__(self):
        return self.title 

