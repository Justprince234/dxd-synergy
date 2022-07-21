from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class Coupon(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=32, unique=True, null=False, editable=False)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_value = models.IntegerField(validators=[MaxValueValidator(100)], verbose_name='Coupon Quantity', null=True) # No. of coupon
    used = models.IntegerField(default=0)
    active = models.BooleanField()
    
    def __str__(self):
        return self.name

    def _generate_coupon_code(self):
        """
        Generate a random, unique coupon code using UUID
        """
        code = uuid.uuid4().hex.upper()
        coupon_number = code[:5]
        return coupon_number
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the coupon code
        if it hasn't been set already.
        """
        if not self.code:
            self.code = self._generate_coupon_code()
        super().save(*args, **kwargs)