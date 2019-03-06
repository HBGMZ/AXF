from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newsdetail/(\d+)/$', views.newsdetail, name='newsdetail'),
    url(r'^bookdetail/(\d+)/$', views.bookdetail, name='bookdetail'),
]