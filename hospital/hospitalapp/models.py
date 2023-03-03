from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    beds_available = models.IntegerField()

    def __str__(self):
        return self.name
