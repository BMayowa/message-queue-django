from django.db import models
import uuid

# Create your models here.
class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(default=None)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Portfolio Model: {self.name}"
