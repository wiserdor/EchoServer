from django.db import models


class Messages(models.Model):
    message = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.message, self.type)
