from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from . import forms

User = get_user_model()


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
