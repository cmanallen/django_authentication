from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
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

  def form_valid(self, form):
    login(self.request, form.get_user())
    if self.request.session.test_cookie_worked():
      self.request.session.delete_test_cookie()

  def form_invalid(self, form):
    return self.render_to_response(self.get_context_data(form=form))

  def get_success_url(self, form):
    return reverse('detail-user', kwargs={'pk': form.get_user()})

class RegisterUser(CreateView):
  """
  Creates an entry in the users model specified in settings.py
  """
  model = AUTH_USER_MODEL
  template_name = 'register.html'
  form_class = UserCreationForm

  def get_context_data(self, *args, **kwargs):
    context = super(CreateUser, self).get_context_data(*args, **kwargs)
    context['action'] = reverse('register-user')
    return context

  def get_success_url(self):
    return reverse('login-user')

class LogoutUser(RedirectView):
  """
  Simple redirect view that destroys the session
  """
  def logout(self, request, *args, **kwargs):
    logout(request)
    return super(LogoutUser, self).logout(request, *args, **kwargs)

  def get_success_url(self):
    return reverse('login-user')
