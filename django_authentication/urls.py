from django.conf.urls import patterns, include, url
import django_authentication.views

urlpatterns = patterns('',
  url(r'^register/$', django_authentication.views.RegisterUser.as_view(),
      name='register-user'),
  url(r'^login/$', django_authentication.views.LoginUser.as_view(),
      name='login-user'),
  url(r'^logout/$', django_authentication.views.LogoutUser.as_view(),
      name='logout-user'),
  url(r'^password/$', django_authentication.views.PasswordChangeUser.as_view(),
      name='password-change-user'),
  url(r'^reset/$', django_authentication.views.PasswordResetUser.as_view(),
      name='password-reset-user'),
)
