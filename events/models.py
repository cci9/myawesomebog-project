from django.db import models

# Create your models here.
class Event(models.Model):
	event_image = models.ImageField(upload_to='events_images/')
	event_char = models.CharField(max_length=300)
