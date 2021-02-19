from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Team object: {self.name} ({self.id})>"

#THE TABLE THAT HAS THE MANY IN THE ONE TO MANY REALTIONSHIP IS THE ONE THAT WILL HAVE THE FOREIGN KEY
class Player(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    pointsPerGame = models.FloatField()
    assignedTeam = models.ForeignKey(Team, related_name="roster", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"<Player object: {self.firstname} ({self.id})>"



