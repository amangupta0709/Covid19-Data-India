from django.db import models



class Registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    statename = models.CharField(max_length=30)
    cityname = models.CharField(max_length=30)

    def __str__(self):
        return self.name


    
