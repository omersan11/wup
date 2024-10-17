from django.db import models

# Create your models here.
from django.db import models

class TextData(models.Model):
    text_input = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_input