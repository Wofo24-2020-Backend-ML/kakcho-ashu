from django.db import models
from django.utils import timezone
from .validators import csv_file_validator
from main.models import User

# Create your models here.

class CSVUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='csvfiles', validators=[csv_file_validator])
    date = models.DateTimeField(default=timezone.now)
    column_name = models.CharField(max_length=25, default= 'Free')
