from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length= 255)
	birthday = models.DateField(max_length= 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return f"<User object: {self.username} ({self.id})>"


class Artist(models.Model):
	firstName = models.CharField(max_length= 255)
	lastName = models.CharField(max_length= 255)
	description = models.TextField(null = True)
	fans = models.ManyToManyField(User, related_name = "likedArtists" )
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"<Artist object: {self.firstName} ({self.id})>"
