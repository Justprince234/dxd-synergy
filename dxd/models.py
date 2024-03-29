from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    """Creates a database instance of Category in database."""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dxd:products_list_by_category', args=[self.slug])

SIZE = (
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
)

class Product(models.Model):
    """Creates a database instance Item in database."""
    available = models.BooleanField(default=True)
    black_friday = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=True)
    best_seller = models.BooleanField(default=False)
    summer = models.BooleanField(default=False)
    travels = models.BooleanField(default=False)
    gift = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    size = models.CharField(choices=SIZE, default= "m", max_length=3)
    color = models.CharField(max_length=50, default="Blue")
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dxd:product', args=[self.slug])

class Career(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Investor(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Investor Site"
    
    def __str__(self):
        return self.title

class HomePageCarousel(models.Model):
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    message1 = models.CharField(max_length=100)
    message2 = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Hompage Message"
    
    def __str__(self):
        return self.name