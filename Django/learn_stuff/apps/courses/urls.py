from django.conf.urls import url
from . import views  


urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/create$', views.new),
    url(r'^courses/edit/(?P<id>\d+)$', views.edit)
]
