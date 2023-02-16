from rest_framework import serializers
from titles.models import Category, Genre, Title, Comment, Review


class UserSerializer(serializers.ModelSerializer):

    pass


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
