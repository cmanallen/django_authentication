from django.conf.urls import patterns, include, url
import django_users.views

urlpatterns = patterns('',
  # Users
  url(r'^register/$', django_users.views.RegisterUser.as_view(),
      name='register-user'),
  url(r'^login/$', django_users.views.LoginUser.as_view(),
      name='login-user'),
  url(r'^logout/$', django_users.views.LogoutUser.as_view(),
      name='logout-user'),
  url(r'^password/$', django_users.views.PasswordChangeUser.as_view(),
      name='password-change-user'),
)
