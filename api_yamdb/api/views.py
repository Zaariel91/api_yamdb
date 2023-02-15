from django.shortcuts import render
from rest_framework import viewsets
from titles.models import Comment, Review
from .serializers import CommentSerializer, ReviewSerializer


class APICommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class APIReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer