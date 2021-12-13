from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    desc = models.TextField()
    price = models.IntegerField()
    slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return self.name

class Images(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product.name

    
class Beads(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='beads/')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    