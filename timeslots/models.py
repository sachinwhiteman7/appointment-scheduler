from django.db import models

from accounts.models import User


class TimeSlot(models.Model):
    """
    Model to represent a timeslot for a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
