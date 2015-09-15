from django.conf.urls import include, url
from portfolioProjrct import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'portfolioProjrct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^zen_mockup/', views.zen, name='zen_mockup'),
    url(r'^forum/', views.forum, name='forum'),
    url(r'^javapic/', include('javapicproject.urls')),
    url(r'^jquerypic/', include('javapicjqproject.urls')),
]
