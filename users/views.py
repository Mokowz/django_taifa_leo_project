from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class ProfileView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = "profile.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)        

