from django.db import models
import jsonfield
# Create your models here.
# Store in db


class Weather(models.Model):
    data = jsonfield.JSONField()

