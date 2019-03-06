import math

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from app.models import Goods

@cache_page(60*5)
def index(request, num=1):
    print('############## 没有缓存(获取数据、渲染模板) #####################')

    goods_list = Goods.objects.all()

    # 总页数
    total_page = math.ceil(goods_list.count() / 12)

    # [0:12]    第1页   0*12 : 1*12
    # [12:24]   第2页   1*12 : 2*12
    # [24:36]   第3页   2*12 : 3*12

    # num第几页
    num = int(num)
    goods_list = Goods.objects.all()[(num-1)*12:num*12]


    # 缓存
    # cache.set(key, value, timeout)
    cache.set('token', '#$%^&*#$%^&*(3456789', timeout=30)


    return render(request, 'index.html', context={'goods_list':goods_list, 'total_page': range(total_page)})


def goods(request, num=1):
    goods_List = Goods.objects.all()

    # 缓存
    # value = cache.get(key)
    token = cache.get('token', '不存在')
    print(token)

    # 分页对象 (数据源，单页数据)
    paginator = Paginator(list(goods_List), 12)

    # 获取当前页对象
    pageObj = paginator.page(num)

    return render(request, 'goods.html', context={'pageObj':pageObj})