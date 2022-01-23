import imp
from django.db.models import query
from rest_framework.generics import ListAPIView
from bookapp.models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes  = [IsAuthenticated]
