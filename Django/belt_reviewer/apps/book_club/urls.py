from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^books$', views.index), 
    url(r'^books/add$', views.book_new), 
    url(r'^review/new$', views.review_new), 
    url(r'^books/(?P<id>\d+)$', views.book_show), 
    url(r'^users/(?P<id>\d+)$', views.user_reviews), 
    url(r'^review/create$', views.review_create), 
    url(r'^review/delete/(?P<id>\d+)$', views.review_destroy), 
]


