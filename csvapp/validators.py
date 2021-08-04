import csv
import os
import io

from django.core.exceptions import ValidationError


def csv_file_validator(value):
    filename, ext = os.path.splitext(value.name)
    if str(ext) != '.csv':
        raise ValidationError("Must be a csv file")
    return True
