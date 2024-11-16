from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):

    CATEGORY_CHOICES = (
        ('NEBULOSA', 'Nebulosa'),
        ('GALAXIA', 'Galaxia'),
        ('PLANETA', 'Planeta'),
        ('ESTRELLA', 'Estrela'),
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, 
        related_name='user', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
