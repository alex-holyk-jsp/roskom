from django.db import models

# Create your models here.
class Domain(models.Model):
    created = models.DateTimeField(auto_now=True)
    domain = models.CharField(max_length=200, blank=True, default='')
    ip = models.CharField(max_length=15)
    owner_ip = models.CharField(max_length=15)

    class Meta:
        ordering = ['created']
