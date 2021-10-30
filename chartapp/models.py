from django.db import models

# Create your models here.

class Products(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    numOfProducts = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.numOfProducts}'
