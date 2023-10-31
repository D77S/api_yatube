from django.urls import path

from rest_framework.authtoken import views

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    # superuser: login/pass admin1/admin1
    # {"token":"d6db9c9a47f413dc44f95a4bac1e9581e19af99f"}
]
