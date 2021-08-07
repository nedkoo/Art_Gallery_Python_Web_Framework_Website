from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from art_gallery_web.gallery_auth.forms import RegisterForm, LogInForm


class RegisterView(CreateView):
    template_name = 'users_arts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return valid


class LogInView(LoginView):
    template_name = 'users_arts/login.html'
    form_class = LogInForm

    redirect_authenticated_user = True

    def get_success_url(self):
        # write your logic here
        if self.request.user.is_superuser:
            return '/admin'
        return '/'


class LogOutView(LogoutView):
    next_page = reverse_lazy('index')
