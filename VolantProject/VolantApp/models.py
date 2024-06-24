from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Footwears(models.Model):
    product_options=(
        ('sandals','sandals'),
        ('slipperandflipflops','slipperandflipflops'),
        ('casualshoes','casualshoes'),
        ('specialcollections','specialcollections'),
        ('flatshoes','flatshoes'),
        ('schooledition','schooledition'),
    )
    product_category=models.CharField(max_length=100,choices=product_options)
    types=(
        ('ladies','ladies'),
        ('gents','gents'),
        ('boys','boys'),
        ('girls','girls'),
        ('kids','kids')
    )
    product_types=models.CharField(max_length=100,choices=types)
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    product_description = models.TextField()
    colors=(
        ('Black','Black'),
        ('Blue','Blue'),
        ('Brown','Brown'),
        ('Camel','Camel'),
        ('Cherry','Cherry'),
        ('Gold','Gold'),
        ('Grape','Grape'),
        ('Green','Green'),
        ('Grey','Grey'),
        ('Maroon','Maroon'),
        ('Mehandi','Mehandi'),
        ('Navy','Navy'),
        ('Olive','Olive'),
        ('Peach','Peach'),
        ('Peacock','Peacock'),
        ('Pink','Pink'),
        ('Purple','Purple'),
        ('Tan','Tan'),
        ('Violet','Violet'),
        ('White','White'),
        ('Wine','Wine'),
        ('Yellow','Yellow'),
    )
    product_color=models.CharField(max_length=100,choices=colors)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.product_name
    
    
class Footwearimages(models.Model):
    product=models.ForeignKey(Footwears,on_delete=models.CASCADE)
    colors=(
        ('Black','Black'),
        ('Blue','Blue'),
        ('Brown','Brown'),
        ('Camel','Camel'),
        ('Cherry','Cherry'),
        ('Gold','Gold'),
        ('Grape','Grape'),
        ('Green','Green'),
        ('Grey','Grey'),
        ('Maroon','Maroon'),
        ('Mehandi','Mehandi'),
        ('Navy','Navy'),
        ('Olive','Olive'),
        ('Peach','Peach'),
        ('Peacock','Peacock'),
        ('Pink','Pink'),
        ('Purple','Purple'),
        ('Tan','Tan'),
        ('Violet','Violet'),
        ('White','White'),
        ('Wine','Wine'),
        ('Yellow','Yellow'),
    )
    product_color=models.CharField(max_length=100,choices=colors)
    product_image=models.ImageField(upload_to='imagesall/',null=True,blank=True)
    
class Footwearsize(models.Model):
    product = models.ForeignKey(Footwears, on_delete=models.CASCADE)
    sizes = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),
    )
    size = models.CharField(max_length=100, choices=sizes)

class CartModel(models.Model):
    product = models.ForeignKey(Footwears, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = (
        ('in_cart', 'in_cart'),
        ('order_placed', 'order_placed'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(max_length=100, choices=choices, default='in_cart')
    size = models.ForeignKey(Footwearsize, on_delete=models.CASCADE)
    color = models.ForeignKey(Footwearimages, on_delete=models.CASCADE)
    total = models.FloatField()
    
    def __str__(self):
        return f"Product: {self.product}, Color: {self.color}, Size: {self.size}"
    

class CartModel(models.Model):
    product = models.ForeignKey(Footwears, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = (
        ('in_cart', 'in_cart'),
        ('order_placed', 'order_placed'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(max_length=100, choices=choices, default='in_cart')
    size = models.ForeignKey(Footwearsize, on_delete=models.CASCADE)
    color = models.ForeignKey(Footwearimages, on_delete=models.CASCADE)
    total = models.FloatField()
    
    def __str__(self):
        return f"Product: {self.product}, Color: {self.color}, Size: {self.size}"
    

class OrderModel(models.Model):
    product = models.ForeignKey(Footwears, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.ForeignKey(Footwearimages, on_delete=models.CASCADE)
    size = models.ForeignKey(Footwearsize, on_delete=models.CASCADE)
    options={
        ('order-placed','order-placed'),
        ('dispatched','dispatched'),
        ('shipped','shipped'),
        ('delivered','delivered'),
        ('cancelled','cancelled')
    }    
    status=models.CharField(max_length=100,choices=options,default='order-placed')
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=100)
    email =models.EmailField(max_length=254)
    address = models.TextField()
    total = models.FloatField()
    
    def __str__(self):
        return f"Product: {self.product}, Color: {self.color}, Size: {self.size}"
    