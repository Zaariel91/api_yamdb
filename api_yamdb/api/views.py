from http import HTTPStatus
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAdminOrReadOnly,
)
from titles.models import Category, Comment, Genre, Review, Title
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    CreateUserSerializer,
    GenreSerializer,
    GetTokenSerializer,
    ReviewSerializer
    TitleSerializer,
)


User = get_user_model()


class APIGetToken(APIView):
    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            user = User.objects.get(username=data['username'])
            confirmation_code = data['confirmation_code']
        except User.DoesNotExist:
            return Response(
                {'username': 'Пользователя не существует'},
                status=status.HTTP_404_NOT_FOUND
            )

        if default_token_generator.check_token(user, confirmation_code):
            token = RefreshToken.for_user(user).access_token
            return Response(
                {'token': str(token)},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'confirmation_code': 'Неверный код подтверждения!'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
def user_create_view(request):
    email = request.data.get('email')
    username = request.data.get('username')
    if User.objects.filter(username=username, email=email).exists():
        send_confirmation_code(username, email)
        return Response(request.data, status=status.HTTP_200_OK)
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    send_confirmation_code(username, email)
    return Response(serializer.data, status=HTTPStatus.OK)


def send_confirmation_code(username, email):
    user = get_object_or_404(User, email=email, username=username)
    confirmation_code = default_token_generator.make_token(user)
    user.confirmation_code = confirmation_code
    MESSAGE = (
        f'Здравствуйте, {username}!'
        f'Ваш код подтверждения: {user.confirmation_code}'
    )
    send_mail(
        message=MESSAGE,
        subject='Confirmation code',
        recipient_list=[user.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
    )
    user.save()


class UserViewSet(viewsets.ModelViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'year', 'category__slug', 'genre__slug')


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


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


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
