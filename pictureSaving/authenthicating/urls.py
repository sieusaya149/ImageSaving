from django.urls import path
from authenthicating import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('register/', views.Register, name="register"),
    path('forget-password/', views.forgetPassPage, name="forget-password"),
    path('change-password/<token>/' , views.ChangePassword , name="change-password"),
]