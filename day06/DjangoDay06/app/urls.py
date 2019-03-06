from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"^register/$", views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^errtest/$', views.errtest, name='errtest'),
    url(r'^lottery/$', views.lottery, name='lottery'),

    url(r'^upfile/$', views.upfile, name='upfile'),
]