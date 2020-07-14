from django.db import models
from django.utils import timezone

# Create your models here.
class News (models.Model):
    author=models.CharField(max_length=15)
    title=models.CharField(max_length=15)
    description=models.TextField()
    pub_date=models.DateField(default=timezone.now())
    def __str__(self):
        return self.author

class SportNews(models.Model):
    author = models.CharField(max_length=15)
    title = models.CharField(max_length=15)
    description = models.TextField()
    def __str__(self):
        return self.author


class RegistrationData(models.Model):
    user=models.TextField(max_length=15)
    password=models.TextField(max_length=15)
    email=models.TextField(max_length=15)
    phone=models.TextField(max_length=15)
    def __str__(self):
        return self.user


