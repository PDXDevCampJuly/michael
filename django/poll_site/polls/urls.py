from django.conf.urls import include, url
from django.contrib import admin
import polls

urlpatterns = [
  url(r'^$', 'polls.views.questions', name='questions'),
  url(r'^(?P<question_id>\d+)/$', 'polls.views.details', name='details')
]
