from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm, PasswordResetForm)
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, RedirectView, FormView

from .mixins import LoginRequiredMixin


class Login(FormView):
    """
    Logs users with the correct credintials in
    """

    model = settings.AUTH_USER_MODEL
    template_name = 'login.html'
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        self.request.session.set_test_cookie()
        return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Register(CreateView):
    """
    Creates an entry in the users model specified in settings.py
    """

    model = settings.AUTH_USER_MODEL
    template_name = 'register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')


class Logout(LoginRequiredMixin, RedirectView):
    """
    Simple redirect view that destroys the session
    """

    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class PasswordChange(LoginRequiredMixin, FormView):
    """
    Updates a user's password field to the entered text
    """
    model = settings.AUTH_USER_MODEL
    template_name = 'change_password.html'
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(PasswordChange, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('login')


class PasswordReset(FormView):
    """
    Email the user with a reset password
    """
    model = settings.AUTH_USER_MODEL
    template_name = 'reset_password.html'
    form_class = PasswordResetForm

    def get_success_url(self):
        return reverse('login')
