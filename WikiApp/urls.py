from django.conf.urls import patterns, url

from WikiApp import views

urlpatterns = patterns('',
    url(r'^$', views.front, name='front'),
	url(r'^login/$', views.front, name='front'),
	url(r'^auth/$', views.auth_view, name='auth_view'),
	url(r'^home/$', views.home, name='home'),
	url(r'^register/$', views.register_user, name='register_user'),
	url(r'^register_success/$', views.register_success, name='register_success'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^digitize/$', views.digitize, name='digitize'),
)