from rest_framework.authtoken import views
from rest_framework import routers

from django.urls import include, path

from .views import PostViewSet


router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet)

#  Для взаимодействия с ресурсами опишите и настройте такие эндпоинты:
#  api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
#  api/v1/posts/ (GET, POST): получаем список всех постов или создаём нов.пост.

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    # superuser: login/pass admin1/admin1
    # {"token":"d6db9c9a47f413dc44f95a4bac1e9581e19af99f"}
]
