from rest_framework import serializers
from .models import CSVUpload
from django.contrib.auth import get_user_model


User = get_user_model()


class CSVUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = CSVUpload
        #fields = ['user', 'file', 'date']
        #read_only_fields = ('user',)

        fields = ['file', 'date', 'column_name']


