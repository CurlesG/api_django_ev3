from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Blogs
from .serializers import BlogsSerializer


class BlogListApiView(APIView):

  def get(self, request, *args, **kwargs):
    blogs = Blogs.objects.all()
    serializer = BlogsSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class NewBlog(APIView):

    auth_check = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion'),
            'autor': request.data.get('autor'),
            'privado': request.data.get('privado'),
            'categoría': request.data.get('categoría'),
            'creado_por': request.user.id,
        }

        serializer = BlogsSerializer(data=data)
        if serializer.is_valid():
            if request.user.is_active == True:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'Response': 'You need to be authenticated to add a new blog'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailApiView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, blog_id, *args, **kwargs):
        blog_instance = Blogs.objects.get(id=blog_id)
        print(blog_instance)
        if blog_instance:
            serializer = BlogsSerializer(blog_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Response': 'Blog does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, blog_id, *args, **kwargs):
        blog_instance = Blogs.objects.get(id=blog_id)

        if not blog_instance:
            return Response({'Response': 'This blog id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion'),
            'autor': request.data.get('autor'),
            'privado': request.data.get('privado'),
            'categoría': request.data.get('categoría'),
        }

        serializer = BlogsSerializer(
            instance=blog_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, blog_id, *args, **kwargs):
        blog_instance = Blogs.objects.get(id=blog_id)
        if blog_instance.creado_por == request.user:
            blog_instance.delete()
            return Response({"Response": "Blog deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"Response": "Only the creator of the Blog can delete."}, status=status.HTTP_400_BAD_REQUEST)