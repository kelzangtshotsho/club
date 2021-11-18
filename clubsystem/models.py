from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Photo(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    description2 = models.CharField(max_length=2000)
    # desc = models.TextField()
    # price = models.IntegerField()
    img = models.ImageField(upload_to ='pics')

    notification = models.CharField(max_length=100, null=True)
    
    
class Record(models.Model):
    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Activity = models.CharField(max_length=100)
    class Meta:
        db_table= "Record"

class Club(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Club = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    def __str__(self):
        return self.Email

    def __str__(self):
        return self.Club

    



