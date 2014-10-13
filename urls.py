from django.conf.urls import url

from .views import Register, Login, Logout, PasswordChange, PasswordReset


urlpatterns = [
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^password/$', PasswordChange.as_view(), name='password-change'),
    url(r'^reset/$', PasswordReset.as_view(), name='password-reset'),
]
