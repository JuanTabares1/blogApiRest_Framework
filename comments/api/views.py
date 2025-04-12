from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from .serializers import CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']