from rest_framework import serializers
from .models import Blogs

class BlogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blogs
        fields = ['id', 'nombre', 'descripcion', 'autor', 'privado', 'categoría', 'creado_por']

