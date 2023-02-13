from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    portfolio_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.username
