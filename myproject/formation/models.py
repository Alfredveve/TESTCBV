from django.db import models

class Formation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    certifier = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.title
