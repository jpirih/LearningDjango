from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError

# Create your models here.

class  Speaker(models.Model):
    name = models.CharField(max_length = 40)
    title = models.CharField(max_length = 50)
    bio = models.TextField(max_length = 1000)
    twitter = models.CharField(max_length = 16, blank = True)
    facebook = models.CharField(max_length = 50, blank = True)
    
    def __str__(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 1000)
    
    def __str__(self):
        return self.title


SESSION_STATUSES = (
     ('a', 'approved'),
     ('s', 'submitted'),
     ('r', 'rejected'), 
)

def validate_nohtml(value):
    if value.index('<') > -1:
        raise ValidationError('Html ni dovoljen')

class Session (models.Model):
    title = models.CharField(max_length = 50)
    abstract = models.TextField(max_length = 2000, validators=[validate_nohtml])
    track = models.ForeignKey(Track)
    speaker = models.ForeignKey(Speaker)
    status = models.CharField(max_length=1,choices = SESSION_STATUSES )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('session_details', kwargs={'pk': self.pk})
