from django.urls import path

from blogs.views import blogs_view, create_blog_post

urlpatterns = [
    path("", blogs_view, name='blogs_view'),
    path("create_blog_post/", create_blog_post, name='create_post'),  # This will redirect to blogs_view for now. Replace with actual view later.
]