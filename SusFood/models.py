from django.db import models

# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to = 'pics/%y/%m/%d')
    title = models.CharField(max_length = 150)
    sustainability = models.IntegerField(default='10')
    minutes = models.IntegerField(default='0')
    price = models.DecimalField(max_digits=5,decimal_places=2,default='0.00')
    
    def _str_(self):
        return self.title
