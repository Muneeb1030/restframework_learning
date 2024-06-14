from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import blogPost
from .serializers import blogPostSerializer

class BlogPostListView(generics.ListCreateAPIView):
    queryset = blogPost.objects.all()
    serializer_class = blogPostSerializer

    def delete(self, request, *args, **kwargs):
        blogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

class BlogPostRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = blogPost.objects.all()
    serializer_class=blogPostSerializer
    lookup_field = 'pk'
