from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/', LoginView.as_view(template_name ='core/login.html'),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('sign-up/', views.SignupView.as_view(),name='sign-up'),
    path('secure/', views.SecureView.as_view(),name='secure'),
    
    
    
    
]
