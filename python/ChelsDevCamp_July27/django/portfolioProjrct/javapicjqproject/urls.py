from django.conf.urls import include, url
from . import views

urlpatterns = [
     url(r'^$', views.jqjavapic, name='jqavapic'),
    # url(r'^join', views.jqjoin, name='jqoin'),
    # url(r'^gallery', views.jqgallery, name='jqgallery')

]