from django.db import models


# 基础类
class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_auth_permissionlength=10)

    class Meta:
        abstract = True


# 轮播图　模型类
# insert into axf_wheel(img,name,trackid)
class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'
