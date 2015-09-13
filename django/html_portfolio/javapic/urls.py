from django.conf.urls import url
from javapic import views

urlpatterns = [
    url(r'^$', views.javapic, name='javapic'),
    url(r'^join/$', views.join, name='join'),
    url(r'^join/gallery/$', views.gallery, name='gallery'),
]
