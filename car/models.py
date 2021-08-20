from django.db import models
from django.utils import timezone

class Car(models.Model):
	year = models.CharField(max_length=400)
	make = models.CharField(max_length=400)
	model = models.CharField(max_length=400)
	price = models.FloatField()
	transmission = models.CharField(max_length=400)
	engine = models.CharField(max_length=400)
	drivetrain = models.CharField(max_length=400)
	weight = models.FloatField()
	mileage = models.FloatField()
	repair_notes = models.CharField(max_length=4000)
	notable_mods = models.CharField(max_length=4000)
	updated = models.DateTimeField(default=timezone.now, blank=True)
