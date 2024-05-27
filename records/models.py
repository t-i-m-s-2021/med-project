from django.db import models

class Record(models.Model):
    fullname = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    localisation = models.TextField(null=True, blank=True)
    author = models.IntegerField(null=True, blank=True)
    visible = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

class Image(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/', null=True, blank=True)