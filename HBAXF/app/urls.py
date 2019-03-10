from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),  # 首页
    url(r'^market/$', views.market, name='market'), # 闪购超市
    url(r'^cart/$', views.cart, name='cart'),   # 购物车
    url(r'^mine/$', views.mine, name='mine'),   # 我的

    url(r'^registe/$', views.registe, name='registe'),  # 注册
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'),  # 验证
    url(r'^logout/$', views.logout, name='logout'),  # 登出
    url(r'^login/$', views.login, name='login'),  # 登录
]
