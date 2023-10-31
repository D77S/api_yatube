from rest_framework.authtoken import views
from rest_framework import routers

from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet, basename='groups')

#  Для взаимодействия с ресурсами опишите и настройте такие эндпоинты:
#  done api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
#  done api/v1/posts/ (GET, POST): получаем список всех постов или создаём нов.пост.
#  только для своих постов, не чужих! (требуется проверка на авторство)
#  !! не получается !!! api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
#  api/v1/groups/ (GET): получаем список всех групп.
#  api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
#  api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
#  api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    # superuser: login/pass admin1/admin1
    # {"token":"d6db9c9a47f413dc44f95a4bac1e9581e19af99f"}
]
