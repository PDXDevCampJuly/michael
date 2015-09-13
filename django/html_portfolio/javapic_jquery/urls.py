from django.conf.urls import url
from javapic_jquery import views

urlpatterns = [
    url(r'^$', views.javapic_query, name="javapic_query"),


]