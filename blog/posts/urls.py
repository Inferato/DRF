from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('posts/', views.BlogPostList.as_view()),
    path('posts/<int:pk>/', views.BlogPostDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('comments/', views.CommentList.as_view())
    ]

urlpatterns = format_suffix_patterns(urlpatterns)