from django.conf.urls import url
from javapic import views

urlpatterns = [
    url(r'^$', views.javapic, name='javapic'),
    url(r'^javapic_join.html', views.join, name='join'),
    url(r'^javapic_gallery.html', views.gallery, name='gallery'),
]
