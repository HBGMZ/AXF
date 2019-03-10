from django.db import models


# 基础类
class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

# 轮播图　模型类
# insert into axf_wheel(img,name,trackid)
class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'


# 导航　模型类
class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'


# 每日必购 模型类
class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'


# 部分商品 模型类
class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


# 商品列表　模型类
# insert into
# (,,,,,,,,,,,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
# values
# (,"25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q","103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q","103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");
class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'


# 商品分类

class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8) # 分类ID
    typename = models.CharField(max_length=100) # 分类名称
    childtypenames = models.CharField(max_length=256)   # 子类名称
    typesort = models.IntegerField()    # 显示先后顺序
    class Meta:
        db_table = 'axf_foodtypes'

# 商品信息
class Goods(models.Model):
    productid = models.CharField(max_length=10) # 商品ID
    productimg = models.CharField(max_length=100)   # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=100)  # 商品弄名称
    isxf = models.BooleanField(default=False)    # 精选
    pmdesc = models.BooleanField(default=False)  # 买一送一
    specifics = models.CharField(max_length=100)   # 规格
    price = models.DecimalField(max_digits=7, decimal_places=2)    # 价格
    marketprice = models.DecimalField(max_digits=7, decimal_places=2)  # 商场价格
    categoryid= models.IntegerField()   # 分类ID
    childcid = models.IntegerField()    # 子类ID
    childcidname = models.CharField(max_length=100) # 分类名称
    dealerid = models.CharField(max_length=10)  # 详情ID
    storenums = models.IntegerField()   # 库存
    productnum = models.IntegerField()  # 销量

    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
#     账号
    account  = models.CharField(max_length=80,unique=True)
# 密码
    password = models.CharField(max_length=256)
    #name
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,unique=True)
    addr = models.CharField(max_length=256)
    img = models.CharField(max_length=100)
    rank = models.IntegerField(default=1)
    token = models.CharField(max_length=256)
    class Meta:
        db_table = 'axf_user'