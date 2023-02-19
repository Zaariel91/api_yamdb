from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.TextField(max_length=256, db_index=True)
    year = models.IntegerField()
    genre = models.ManyToManyField(
        Genre,
        related_name="titles", blank=True, null=True
    )
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name="titles",blank=True, null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    score = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews'
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=['title', 'author'], name='unique_review')
        ]
        
       
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )

    def __str__(self) -> str:
        return self.text
