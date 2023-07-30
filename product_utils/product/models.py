from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/')

    def __str__(self):
        return f"Image id: {self.id}"


class Product(models.Model):

    class Condition:
        new = 'new'
        used = 'used'

    CONDITION_CHOICES = (
        (Condition.new, "new"),
        (Condition.used, "used")
    )

    product_name = models.CharField(max_length=300, unique=True)
    product_description = models.TextField()
    SKU = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    main_image = models.ImageField(
        upload_to='product_images/%Y/%m/%d/', blank=True, null=True
    )
    additional_images = models.ManyToManyField('Image', blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_reviews = models.PositiveIntegerField(default=0)
    condition = models.CharField(max_length=5, choices=CONDITION_CHOICES, blank=True, null=True)
    warranty = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.product_name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.product_name}"


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"Rating for {self.product.product_name}"
