from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #queryset = Category.objects.filter(published=True)
    queryset = Category.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']