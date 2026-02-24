from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.db import models

class Vendor(models.Model):
    id = models.CharField(
        max_length=20,
        primary_key=True
    )
    name = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "vendor"
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    def __str__(self):
        return f"{self.id} - {self.name}"
    


class Product(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex'),
    ]

    # Manual 6-digit ID
    id = models.IntegerField(
        primary_key=True, 
        validators=[MinValueValidator(100000), MaxValueValidator(999999)]
    )
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MeasurementMaster(models.Model):
    name = models.CharField(max_length=100) # e.g., "Chest", "Sleeve"
    unit = models.CharField(max_length=20, default="inches") # e.g., "cm", "inches"

    def __str__(self):
        return f"{self.name} ({self.unit})"

class ProductMeasurementMap(models.Model):
    # Links to your existing Product model
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    # Links to the Measurement Master
    measurement = models.ForeignKey(MeasurementMaster, on_delete=models.CASCADE)
    
    is_required = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']
        # Prevents mapping the same measurement to the same product twice
        unique_together = ('product', 'measurement')

    def __str__(self):
        return f"{self.product.name} - {self.measurement.name}"

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_synced = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PaymentMode(models.Model):
    name = models.CharField(max_length=100)
    is_cash = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name