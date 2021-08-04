from django.urls import path

from .views import GoogleSocialAuthView, Home

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),

]
