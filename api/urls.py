from django.urls import path
from .views import BlogListApiView, NewBlog, BlogDetailApiView

urlpatterns = [
    path('blogs/', BlogListApiView.as_view()),
    path('blogs/new', NewBlog.as_view()),
    path('blogs/<int:blog_id>/', BlogDetailApiView.as_view()),
]