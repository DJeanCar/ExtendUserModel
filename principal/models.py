from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User , unique=True)
	# extra atributos
	bio = models.TextField(null=True)
	direccion = models.CharField(null=True , max_length=100)
	telefono = models.CharField(max_length=20)
	def __unicode__(self):
		return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)	

from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)	