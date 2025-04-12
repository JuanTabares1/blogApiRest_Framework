from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()