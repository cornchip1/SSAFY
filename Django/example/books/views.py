from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse


from .serializers import BookListSerializer, BookSerializer
from .models import Book

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many = True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)
    

