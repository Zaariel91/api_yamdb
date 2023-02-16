from rest_framework import routers

from django.urls import include, path
from .views import ReviewViewset, TitleViewset, CommentViewset

router = routers.DefaultRouter()
router.register(r'titles', TitleViewset)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewset, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
                CommentViewset, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
