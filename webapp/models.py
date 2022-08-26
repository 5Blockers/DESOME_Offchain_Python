from django.db import models

# Create your models here.
class ImageChecker(models.Model):
    min_dist = models.IntegerField(default=64)
    flag = models.BooleanField(default=False)
    result_link = models.TextField()
