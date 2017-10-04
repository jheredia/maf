from django.db import models
from django.utils import timezone

class Femicidio(models.Model):
	author = models.ForeignKey('auth.User')
	created_date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=64)
	age = models.PositiveIntegerField()
	city = models.CharField(max_length=64)
	province = models.CharField(max_length=64)
	country = models.CharField(default='Argentina', editable=False, max_length=32)
	latitude = models.CharField(max_length=64)
	longitude = models.CharField(max_length=64)

	def __str__(self):
		return self.name



