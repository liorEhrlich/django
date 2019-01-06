from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list', views.list, name='index'),
    url(r'^add', views.add, name='index'),
    url(r'^get', views.get, name='index'),
]
