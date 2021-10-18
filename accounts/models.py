from django.db import models
from django.contrib.auth.models import AbstractUser


INTERVIEWER = 'interviewer'
CANDIDATE = 'candidate'

USER_TYPE_CHOICES = (
    (INTERVIEWER, 'Interviewer'),
    (CANDIDATE, 'Candidate')
)


class User(AbstractUser):
    """
    Model to represent a User,
    Fields from AbstractUser are used, user_type field is added to differentiate between Interviewer and Candidate.
    """

    user_type = models.CharField(max_length=16, choices=USER_TYPE_CHOICES, default=INTERVIEWER)



