from django.db import models

# Create your models here.
class ChartData(models.Model):
    dateTime = models.DateTimeField("YYYY-MM-DD HH:MM:ss")
    value = models.IntegerField()

    def __str__(self):
        return f"{self.dateTime}: {self.value}"
