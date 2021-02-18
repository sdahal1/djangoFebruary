from django.db import models

# Create your models here.
class TvShow(models.Model):
    #field names go here
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)




