from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from .validators import validate_username
from titles.models import Category, Genre, Title, Comment, Review

User = get_user_model()


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[
            validate_username,
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=(
            validate_username,
            UniqueValidator(queryset=User.objects.all(), ),
        ),
        max_length=150,
        required=True
    )
    email = serializers.EmailField(
        validators=(
            UniqueValidator(queryset=User.objects.all()),
        ),
        max_length=254,
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email')
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    review = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        fields = '__all__'
        model = Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    title = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        fields = '__all__'
        model = Review
