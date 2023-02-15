from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from titles.models import Comment, Review, Title
from .serializers import CommentSerializer, ReviewSerializer, TitleSerializers


class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            review_id=self.kwargs.get('review_id')
        )

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        author = self.request.user
        serializer.save(author=author, review=review)

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            title_id=self.kwargs.get('title_id')
        )

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        author = self.request.user
        serializer.save(author=author, title=title)


class TitleViewset(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializers