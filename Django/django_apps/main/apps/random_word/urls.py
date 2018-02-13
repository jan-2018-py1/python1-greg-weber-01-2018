from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^random_word/$', views.random_word),
    url(r'^random_word/generate_new$', views.generate_new),
    url(r'^random_word/reset$', views.reset_counter)    
  ]