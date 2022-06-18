from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db import models

# Create your models here.



class Post(models.Model):
    Title = models.CharField(max_length=200, blank=False, null=False)
    Text = models.TextField()
    Author = get_user_model()
    Created_date = models.DateTimeField('date created')
    Published_date = models.DateTimeField('date published')
