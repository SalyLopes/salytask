from django.db import models



class Task(models.Model):
    item = models.CharField(max_length=20)
    status=  models.CharField(max_length=20)

    def __str__(self):
        return self.item