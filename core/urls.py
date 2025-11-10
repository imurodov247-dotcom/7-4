from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/', LoginView.as_view(template_name ='core/login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('sign-up/', views.SignupView.as_view(),name='sign-up'),
    path('secure/', views.SecureView.as_view(),name='secure'),
    path('create/', views.PostCreateView.as_view(),name='post-create'),
    path('posts/', views.PostListView.as_view(),name='posts'),
    path('post-delete/<int:pk>', views.PostDeleteView.as_view(),name='post-delete'),
    
    
    
    
]
