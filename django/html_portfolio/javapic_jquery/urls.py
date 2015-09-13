from django.conf.urls import url
from javapic_jquery import views

urlpatterns = [
    url(r'^$', views.javapic_jquery, name='javapic_jquery'),
]