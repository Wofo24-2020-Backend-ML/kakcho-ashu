from django.urls import path
from .views import RegisterView, LogoutAPIView, SetNewPasswordAPIView, LoginAPIView, PasswordTokenCheckAPI
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('new password-set-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
