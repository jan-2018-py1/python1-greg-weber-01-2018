from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^books_authors$', views.index)     
]