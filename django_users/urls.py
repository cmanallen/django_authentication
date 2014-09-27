from django.conf.urls import patterns, include, url
import django_users.views

urlpatterns = patterns('',
  # Users
  url(r'^register/$', django_users.views.RegisterUser.as_view(),
      name='create-user'),
  url(r'^login/$', django_users.views.LoginUser.as_view(),
      name='update-user'),
  url(r'^logout/$', django_users.views.LogoutUser.as_view(),
      name='delete-user'),
)
