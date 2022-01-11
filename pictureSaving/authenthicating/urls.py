from django.urls import path
from authenthicating import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.Register, name="register"),
    path('forget-password/', views.forgetPassPage, name="forget-password"),
    path('change-password/<token>/' , views.ChangePassword , name="change-password"),
]