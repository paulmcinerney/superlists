from django.conf.urls import patterns, include, url
from django.contrib import admin
from lists import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^(\d+)/$', views.view_list,name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^new$', 'lists.views.new_list', name='new_list'),
    #url(r'^admin/', include(admin.site.urls)),
)
