#coding=utf-8

from django.db import models
from juser.models import *

# Create your models here.


class JProject(models.Model):
    """
        项目
    """
    PRO_STATUS = (
        (0, 'Normal'),
        (1, 'Delay'),
    )
    name = models.CharField(max_length=255)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    status = models.IntegerField(choices=PRO_STATUS, default=0)
    comment = models.CharField(max_length=100, blank=True, null=True)


class JMileStone(models.Model):
    """
        里程碑
    """
    MS_STATUS = (
        (0, 'Normal'),
        (1, 'Delay'),
    )
    name = models.CharField(max_length=255)
    project = models.ForeignKey(JProject)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    status = models.IntegerField(choices=MS_STATUS, default=0)
    comment = models.CharField(max_length=100, blank=True, null=True)
    parent_node = models.IntegerField(default=0)
