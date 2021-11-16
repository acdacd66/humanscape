from django.db import models
from django.utils import timezone
from model_utils import FieldTracker

# Create your models here.
class ClinicalData(models.Model):
    taskCode = models.CharField(max_length=100,null=True,unique=True)
    taskName = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)
    chiefInstitution = models.CharField(max_length=100,null=True)
    studySubjectNumbers = models.IntegerField(null= True)
    studyPeriod = models.IntegerField(null= True)
    studyType = models.CharField(max_length=100,null=True)
    studyPhase = models.CharField(max_length=100,null=True)
    studyScope = models.CharField(max_length=100,null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at = models.DateField(auto_now_add=False,null=True)

    tracker = FieldTracker()