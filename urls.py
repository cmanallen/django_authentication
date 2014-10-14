from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password/$', views.PasswordChangeView.as_view(), name='password-change'),
    url(r'^reset/$', views.PasswordResetView.as_view(), name='password-reset'),
]
