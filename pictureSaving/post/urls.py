from django.urls import path
from post import views
urlpatterns = [
    path('', views.index, name="index"),
    path('api/getPostInfo/<postId>/', views.getPostInfor),
    path('api/getImageInfo/<postId>/', views.getImageInfor),
    path('api/getHeartInfo/<postId>/',views.getHeartInfor),
    path('api/getCommentInfo/<postId>/',views.getCommentInfor),
    path('post', views.CreateNewPost, name="create-post")
]