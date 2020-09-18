from django.db import models

STATUS_CHOICES = [
    ('requested', 'requested'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
]


# Create your models here.
class Domain(models.Model):
    created = models.DateTimeField(auto_now=True)
    domain = models.CharField(max_length=200, blank=True, default='')
    ip = models.CharField(max_length=15)
    owner_ip = models.CharField(max_length=15)
    owner_email = models.EmailField(max_length=200)
    status=models.CharField(choices=STATUS_CHOICES, default='requested', max_length=50)

    class Meta:
        ordering = ['created']
