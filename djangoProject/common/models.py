from django.contrib.auth.models import User
from django.db import models


class EmailsNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    email = models.CharField(max_length=150, unique=True, null=False, blank=False)
