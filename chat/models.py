from django.db import models


class Message(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    message = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)
