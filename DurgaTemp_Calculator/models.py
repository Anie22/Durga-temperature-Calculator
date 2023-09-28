from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class History(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    temperature = models.FloatField()
    from_unit = models.CharField(max_length=25)
    converted = models.FloatField()
    to_unit = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f'Conversion from: {self.from_unit} to {self.to_unit} on {self.created_at}'