from django.conf.urls import url
from javapic_jquery import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join', views.join, name='join'),
    url(r'^gallery', views.gallery, name='gallery'),
]
