from django.db import models
from django.utils import timezone

class Car(models.Model):
	name = models.CharField(max_length=400)
	price = models.FloatField()
	transmission = models.CharField(max_length=400)
	engine = models.CharField(max_length=400)
	drivetrain = models.CharField(max_length=400)
	weight = models.FloatField()
	needs_fixin = models.CharField(max_length=4000)
	updated = models.DateTimeField(default=timezone.now, blank=True)
