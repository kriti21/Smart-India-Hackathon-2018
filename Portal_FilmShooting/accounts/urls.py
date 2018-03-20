from . import views
from django.conf import settings
from django.urls import path, re_path

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^login/$', views.login_view, name='login_view'),
	re_path(r'^logout/$', views.logout_view, name='logout_view'),
	re_path(r'^register/$', views.register, name='register'),
]