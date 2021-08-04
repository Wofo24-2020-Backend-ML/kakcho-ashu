from django.contrib import admin
from django.urls import path, include
from main import views as mainviews
from rest_framework import permissions
from frontend import views as v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('main.urls')),
    #path("", include('frontend.urls')),
    path('csvupload/', include('csvapp.urls')),
    path('google_auth/', include(('googleauth.urls', 'googleauth'),namespace="googleauth")),

    path('', v1.home),
    path('googleauth/', v1.GoogleAuth),
    path('postgoogletoken/', v1.posttoken),
    path('signupf/', v1.signupf),
    path('loginf/', v1.loginf),
    path('task1/', v1.task1),
]
