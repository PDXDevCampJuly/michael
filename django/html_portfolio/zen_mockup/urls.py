from django.conf.urls import url
from zen_mockup import views

urlpatterns = [
    url(r'^$', views.zen_mockup, name='zen_mockup'),

]