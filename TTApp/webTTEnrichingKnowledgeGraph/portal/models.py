from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# choices option
Type_CHOICES = (
        ('external', 'External'),
        ('local', 'Local'),
    )


# Create your models here.
class repositoryNew(models.Model):
    idrepository = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=4000, blank=True, choices=Type_CHOICES)
    nameRepository = models.CharField(max_length=4000, blank=True)
    resource = models.FileField(upload_to='portal/data/')
    state = models.IntegerField()

    def __str__(self):
        return self.nameRepository + ' |' + self.origin

    class Meta:
        db_table = 'repositoryNew'


class DataTurtel(models.Model):
    idDataTurtel = models.AutoField(primary_key=True)
    DataSemantic = models.FileField(upload_to='portal/data/')
    nameResource = models.CharField(max_length=4000, blank=True)

    def __str__(self):
        return self.nameResource + ' |' + self.DataSemantic

    class Meta:
        db_table = 'DataTurtel'