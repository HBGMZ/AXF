from django.db import models

# 用户模型类
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    sex = models.CharField(max_length=4)

