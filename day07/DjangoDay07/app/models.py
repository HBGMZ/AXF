from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=255)
    price = models.IntegerField()
    detail = models.CharField(max_length=255)

    class Meta:
        db_table = 'goods'


    # def __str__(self):
    #     return '{}-{}-{}'.format(self.id, self.name, self.price)


class Grade(models.Model):
    g_name = models.CharField(max_length=40)

    def __str__(self):
        return self.g_name


class Student(models.Model):
    s_name = models.CharField(max_length=40)
    s_score = models.IntegerField(default=0)

    s_grade = models.ForeignKey(Grade)
