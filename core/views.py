from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView
from .forms import SignupForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def index(request):
    return render(request,"core/index.html")


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'core/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
    
    
class SecureView(TemplateView):
    template_name = 'core/secure.html'
    
class SignupView(FormView):
    template_name = 'core/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        authenticate(self.request,username-username,password=password  )
        if user:
            login(self.request,user)
            
        return super().form_valid(form)
    