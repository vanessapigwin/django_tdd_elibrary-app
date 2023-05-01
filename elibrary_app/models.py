from django.db import models

class Catalogue(models.Model):

    STATUS_CHOICES = (
        ('true', 'True'),
        ('false', 'False'),
    )

    title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=20)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=5, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
