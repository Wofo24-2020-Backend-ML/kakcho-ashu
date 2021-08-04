from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from csvapp import views
from django.urls import path, include



urlpatterns = [

    path('task2/', views.CSVTASK2View.as_view(), name='CSVviewSet2'),
    path('task3', views.CSVTASK3View.as_view(), name='CSVviewSet3'),
    path('task4', views.CSVTASK4View.as_view(), name='CSVviewSet4'),
]
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
