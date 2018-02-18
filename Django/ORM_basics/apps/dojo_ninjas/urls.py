from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^dojo_ninjas$', views.index)     
]