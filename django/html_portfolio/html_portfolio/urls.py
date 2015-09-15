from django.conf.urls import include, url
from django.contrib import admin

    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # -----------------------------------------------

urlpatterns = [
    url(r'^javapic/', include('javapic.urls')),
    url(r'^javapic_jquery/', include('javapic_jquery.urls')),
    url(r'^zen_mockup/', include('zen_mockup.urls')),
    url(r'^forum/', include('forum.urls')),

    # new url patterns should be coded above
    url(r'^', include('about.urls')),
]
