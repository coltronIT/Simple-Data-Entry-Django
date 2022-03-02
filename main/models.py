from django.db import models

# Create your models here.
class DataEntryItems(models.Model):
    name = models.CharField(max_length=200, default="unlisted")
    age = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default="unlisted")
    hometown = models.CharField(max_length=200, default="unlisted")

    def __str__(self):
        return self.name