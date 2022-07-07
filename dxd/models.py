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