from django.conf.urls import url
from javapic import views

urlpatterns = [
    url(r'^$', views.javapic, name='javapic'),
]
