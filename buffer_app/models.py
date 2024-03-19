from django.db import models

# Create your models here.
class Publication(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='publications/')
    description = models.TextField()

    def __str__(self):
        return self.name
