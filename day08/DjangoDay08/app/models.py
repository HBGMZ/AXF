from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    n_title = models.CharField(max_length=100)
    n_time = models.DateTimeField(auto_now=True)

    # 富文本定制
    # n_content = models.TextField()
    n_content = HTMLField()

    def __str__(self):
        return self.n_title


class Book(models.Model):
    b_title = models.CharField(max_length=100)
    b_time = models.DateTimeField(auto_now=True)
    b_content = models.TextField()

    def __str__(self):
        return self.b_title