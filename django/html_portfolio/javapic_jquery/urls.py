from django.conf.urls import url
from javapic_jquery import views

urlpatterns = [
    url(r'^$', views.javapic_jquery, name='javapic_jquery'),
    url(r'^join/$', views.join, name='join'),
    url(r'^join/gallery/$', views.gallery, name='gallery'),
]