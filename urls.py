from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^register/$', views.RegisterUser.as_view(), name='register-user'),
  url(r'^login/$', views.LoginUser.as_view(), name='login-user'),
  url(r'^logout/$', views.LogoutUser.as_view(), name='logout-user'),
  url(r'^password/$', views.PasswordChangeUser.as_view(),
    name='password-change-user'),
  url(r'^reset/$', views.PasswordResetUser.as_view(),
    name='password-reset-user'),
]
