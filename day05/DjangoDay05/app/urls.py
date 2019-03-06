from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # 正则表达式
    url(r'^goods/$', views.goods, name='goods'),    # 默认第一页
    url(r'^goods/(\d+)/$', views.goods, name='goodslist'),
    url(r'^sum/(\d+)/(\d+)/(\d+)/$', views.sum, name='sum'),

    # 标识清楚参数名
    url(r'^detail/(\w+)/$', views.detail, name='detail'),
    url(r'^detail/(?P<name>\w+)/$', views.detail, name='detail'),

    url(r'^gettest/$', views.gettest, name='gettest'),
    url(r'^postview/$', views.postview, name='postview'),
    url(r'^posttet/$', views.posttet, name='posttet'),

    url(r'^urltest/$', views.urltest, name='urltest'),

    url(r'^jsontest/$', views.jsontest, name='jsontest'),


    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
]