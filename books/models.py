from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # New price field

    def __str__(self):
        return self.title
