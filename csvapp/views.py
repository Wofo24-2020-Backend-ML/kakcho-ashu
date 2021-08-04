from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .serializer import CSVUploadSerializer
from .models import CSVUpload
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .permission import *
import pandas as pd
import io
from csv import DictReader
import csv
from django.http import HttpResponse
from .csvfunc import *

from rest_framework.views import APIView
import math
from django.views.decorators.csrf import csrf_exempt

import time


class CSVTASK2View(APIView):
    serializer_class = CSVUploadSerializer
    # permission_classes = (permissions.IsAuthenticated,IsAdmin)
    queryset = CSVUpload.objects.all()

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['file']
        type = serializer.validated_data['column_name']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        try:
            df_data_column = pd.read_csv(io_string, delimiter=',', index_col=0,
                                         names=['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
                                                'Price',
                                                'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
                                                'Android Ver'])

            if type != 'All':
                type_func = lambda type: 'Type=="' + type + '"'
                paid_app_data = df_data_column.query(type_func(type))
                response = HttpResponse(paid_app_data.to_csv(), content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=result.csv'
                return response

            else:
                response = HttpResponse(df_data_column.to_csv(), content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=result.csv'
                return response

        except:
            Response({'error': 'Oops Something Bad, actually you uploaded the wrong file that was not expected'},
                     status=status.HTTP_400_BAD_REQUEST)




class CSVTASK3View(APIView):
    serializer_class = CSVUploadSerializer
    permission_classes = (permissions.IsAuthenticated,IsAdmin)
    queryset = CSVUpload.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['file']
        content_rating = serializer.validated_data['column_name']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        try:
            df_data_column = pd.read_csv(io_string, delimiter=',', index_col=0,
                                         names=['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
                                                'Price',
                                                'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
                                                'Android Ver'])

            try:
                if content_rating in [i for i in df_data_column['Content Rating'].unique()]:
                    dff = df_data_column[df_data_column['Content Rating'] == content_rating]
                    response = HttpResponse(dff.to_csv(), content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename=result.csv'
                    return response

            except:
                HttpResponse({'error': 'Oops Something Bad, actually you uploaded the wrong file that was not expected'},
                         status=status.HTTP_400_BAD_REQUEST)



        except:
            HttpResponse({'error': 'Oops Something Bad, actually you uploaded the wrong file that was not expected'},
                         status=status.HTTP_400_BAD_REQUEST)



class CSVTASK4View(APIView):
    serializer_class = CSVUploadSerializer
    # permission_classes = (permissions.IsAuthenticated,IsAdmin)
    queryset = CSVUpload.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CSVUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        try:
            df_data_column = pd.read_csv(io_string, delimiter=',', index_col=0,
                                         names=['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
                                                'Price',
                                                'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
                                                'Android Ver'])

            df_data_column['Rating Roundoff'] = df_data_column['Rating'].apply(myfunc)
            response = HttpResponse(df_data_column.to_csv(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=result.csv'
            return response

        except:
            HttpResponse({'error': 'Oops Something Bad, actually you uploaded the wrong file that was not expected'},
                         status=status.HTTP_400_BAD_REQUEST)



def myfunc(x):
  x = float(x)
  if math.isnan(x):
    y=0
  else:
    y=round(x)
  return y