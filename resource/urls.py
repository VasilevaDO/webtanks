from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    (r'^latest/$', views.index),
)
