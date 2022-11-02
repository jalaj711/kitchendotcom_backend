from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogandnews, name="blogandnews"),
    path('blog/<int:blogId>', views.blog, name="blog"),
    path('blog/<int:blogId>/', views.blog, name="blog2"),
    path('blog/like/<int:blogId>', views.blog_like, name="blog_like"),
    path('blog/like/<int:blogId>/', views.blog_like, name="blog_like2"),
    # API to post a comment
    path('blog/comment/<int:blogId>', views.comments, name="comments"),
    path('blog/comment/<int:blogId>/', views.comments, name="comments2"),
]
