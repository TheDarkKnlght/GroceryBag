from django.db import models
from django.conf import settings
from django.utils import timezone

status_choices = (('B', 'Bought'),('P', 'Pending'),('NA', 'Not Available'),)

class Item(models.Model) :
    name = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    status = models.CharField(
        max_length = 15,
        choices=status_choices,
        default = 'P'
        )
    date = models.DateField()
