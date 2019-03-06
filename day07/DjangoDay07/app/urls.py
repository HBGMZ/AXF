from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<num>\d+)/$', views.index, name='index'),
    url(r'^goods/(\d+)/$', views.goods, name='goods')
]