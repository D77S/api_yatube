from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet, basename='groups')
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments'
                )

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    # superuser: login/pass admin1/admin1
    # {"token":"d6db9c9a47f413dc44f95a4bac1e9581e19af99f"}
]
