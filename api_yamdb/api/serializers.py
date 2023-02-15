from rest_framework import serializers
from titles.models import Comment, Review, Title


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


class TitleSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title