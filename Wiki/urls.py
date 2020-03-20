from django.urls import path,include
from django.conf.urls import include, url
# from Wiki.views import *
from Wiki import views as Wiki_views
from Wiki import views


urlpatterns = [

url(r'^wiki/(?P<page_name>[^/]+)/edit/$', views.edit_page),
url(r'^wiki/(?P<page_name>[^/]+)/save/$', views.save_page),
url(r'^wiki/(?P<page_name>[^/]+)/$', views.view_page),

]