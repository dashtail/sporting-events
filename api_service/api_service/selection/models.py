from django.db import models
from api_service.event.models import Event

OUTCOME_CHOICES = (
    ('u','Unsettled'),
    ('v','Void'),
    ('L','Lose'),
    ('w','Win'),
)


class Selection(models.Model):
    name = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    outcome = models.CharField(max_length=1, choices=OUTCOME_CHOICES)
    active = models.BooleanField(default=False)
    


