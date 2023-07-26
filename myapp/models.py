from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Services(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="imagenes",null=True)

    def __str__(self) -> str:
        return self.title