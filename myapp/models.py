from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_image = models.CharField(max_length=500,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbuxTvLmcRQ0jT24UR5jTxeYkxOyjfy4ylH_Yx-pmEKw&s=10')
    
    def __str__(self):
        return self.item_name