from django.conf.urls import url
from javapic import views

urlpatterns = [
    url(r'^$', views.javapic, name='javapic'),
    url(r'^join.html', views.join, name='join'),
    url(r'^gallery.html', views.gallery, name='gallery'),
]
