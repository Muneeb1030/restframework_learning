from django.urls import path
from .views import BlogPostListView, BlogPostRUD

urlpatterns = [
    path('',BlogPostListView.as_view(), name='blogpost_view_create'),
    path('blogpost/<int:pk>/',BlogPostRUD.as_view(), name='blogpost-view-rud')
]
