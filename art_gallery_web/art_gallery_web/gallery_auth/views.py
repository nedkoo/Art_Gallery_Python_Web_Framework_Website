from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from art_gallery_web.gallery_auth.forms import RegisterForm, LogInForm, UserProfileForm
from art_gallery_web.gallery_auth.models import UserProfile


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


class UserProfileView(UpdateView):
    template_name = 'users_arts/profile_user.html'
    form_class = UserProfileForm
    model = UserProfile
    success_url = reverse_lazy('my_profile')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk', None)

        if pk is None:
            user = self.request.user
        else:
            user = User.objects.get(pk=pk)

        if self.request.user.is_superuser:
            raise Http404

        return user.userprofile

    def get_context_data(self, **kwargs):
        can_upload = False
        context = super().get_context_data(**kwargs)
        arts = self.get_object().user.arts_set.all()
        context['art_user'] = self.get_object().user

        for art in arts:
            if art.created_by_id == self.request.user.id:
                can_upload = True

            art.can_modify = art.created_by_id == self.request.user.id

        context['arts'] = arts
        context['can_upload'] = can_upload

        return context
