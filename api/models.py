from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
    categ = (
    ('tech', 'tech'),
    ('offtopic', 'offtopic'),
    ('hardware', 'hardware'),
    ('software','software'),
    )
    nombre = models.CharField(null = False, max_length = 100)
    descripcion = models.CharField(null = False, max_length = 500)
    autor = models.CharField(null = False, max_length = 100)
    privado = models.BooleanField()
    categoría = models.CharField(max_length=255, choices=categ, blank = True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, null = True)