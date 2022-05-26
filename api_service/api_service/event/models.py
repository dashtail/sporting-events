from django.db import models
from api_service.sport.models import Sport

EVENT_TYPES_CHOICES = (
    ('pre','preplay'),
    ('in','inplay'),
)

EVENT_STATUS_CHOICES = (
    ('p', 'Pending'), 
    ('s', 'Started'), 
    ('e', 'Ended'),
    ('c', 'Cancelled')
)

class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)
    type =  models.CharField(max_length=3, choices=EVENT_TYPES_CHOICES)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=EVENT_STATUS_CHOICES)
    scheduled_start = models.DateTimeField()
    actual_start = models.DateTimeField(blank=True, null=True)
