from django.shortcuts import render_to_response
from django.views.generic import CreateView, RedirectView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django_authentication.utils import LoginRequiredMixin


from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class LoginUser(FormView):
  """
  Logs users with the correct credintials in
  """
  model = AUTH_USER_MODEL
  template_name = 'login.html'
  form_class = AuthenticationForm

  def dispatch(self, request, *args, **kwargs):
    self.request.session.set_test_cookie()
    return super(LoginUser, self).dispatch(request, *args, **kwargs)

  def get_context_data(self, *args, **kwargs):
    context = super(LoginUser, self).get_context_data(*args, **kwargs)
    context['action'] = reverse('login-user')
    return context

  def form_valid(self, form):
    login(self.request, form.get_user())
    if self.request.session.test_cookie_worked():
      self.request.session.delete_test_cookie()
    return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

  def form_invalid(self, form):
    return self.render_to_response(self.get_context_data(form=form))

class RegisterUser(CreateView):
  """
  Creates an entry in the users model specified in settings.py
  """
  model = AUTH_USER_MODEL
  template_name = 'register.html'
  form_class = UserCreationForm

  def get_context_data(self, *args, **kwargs):
    context = super(RegisterUser, self).get_context_data(*args, **kwargs)
    context['action'] = reverse('register-user')
    return context

  def get_success_url(self):
    return reverse('login-user')

class LogoutUser(LoginRequiredMixin, RedirectView):
  """
  Simple redirect view that destroys the session
  """
  url = reverse_lazy('login-user')

  def dispatch(self, request, *args, **kwargs):
    url = self.get_redirect_url(*args, **kwargs)
    logout(request)
    return HttpResponseRedirect(url)

class PasswordChangeUser(LoginRequiredMixin, FormView):
  """
  Updates a user's password field to the entered text
  """
  model = AUTH_USER_MODEL
  template_name = 'change_password.html'
  form_class = PasswordChangeForm

  def dispatch(self, *args, **kwargs):
    return super(PasswordChangeUser, self).dispatch(*args, **kwargs)

  def get_form_kwargs(self):
    kwargs = super(PasswordChangeUser, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def get_success_url(self):
    return reverse('login-user')

class PasswordResetUser(FormView):
  """
  Email the user with a reset password
  """
  model = AUTH_USER_MODEL
  template_name = 'reset_password.html'
  form_class = PasswordResetForm

  def get_context_data(self, *args, **kwargs):
    context = super(PasswordResetUser, self).get_context_data(*args, **kwargs)
    context['action'] = reverse('password-reset-user')
    return context

  def get_success_url(self):
    return reverse('login-user')
