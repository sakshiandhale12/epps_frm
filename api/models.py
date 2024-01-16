# models.py
from django.db import models


class PiAddress(models.Model):
    id = models.AutoField(primary_key=True)
    addtype = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        db_table = 'pi_address'  # Specify the actual table name
        app_label = 'public'  # Replace with your app name if needed



# class CommonFields(models.Model):
#     createdBy = models.CharField(max_length=255)
#     updatedBy = models.CharField(max_length=255)
#     approvedBy = models.CharField(max_length=255)
#     isActive = models.BooleanField(default=True)

#     class Meta:
#         abstract = True