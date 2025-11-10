from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView,ListView,DeleteView
from .forms import SignupForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from .forms import PostCreateForm
from .models import Post
from django.contrib.auth.models import Group
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
        
        group = Group.objects.get_or_create('users')
        
        user.groups.add(group)
        user.save()
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        authenticate(self.request,username-username,password=password  )
        if user:
            login(self.request,user)
            
        return super().form_valid(form)
    
    
class PostCreateView(PermissionRequiredMixin,LoginRequiredMixin,FormView):
    template_name = 'core/post-create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('posts')
    permission_required = 'core.add_post'
    raise_exception = True
    
    def form_valid(self, form):
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        Post.objects.create(title=title,content=content,author = self.request.user)
        return super().form_valid(form)
    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    permission_required = 'core,delete-post'
    raise_exception = True
    
    def test_func(self):
        user = self.request.user
        author = self.get_object().author
        print("user", user)
        print("author",author)
        return user.has_perm('core.delete.post') and  user==author
    
class PostListView(ListView):
    template_name = 'core/post_list.html'
    model = Post
    context_object_name = 'posts'