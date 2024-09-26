from core.mixins import ActionBasedViewSetMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoView(ActionBasedViewSetMixin, GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Todo.objects.all()
    queryset_map = {
        "list": TodoSerializer.get_optimized_queryset(),
        "partial_update": TodoSerializer.get_optimized_queryset(),
        "destroy": TodoSerializer.get_optimized_queryset(),
    }
    serializer_class = TodoSerializer
    serializer_class_map = {
        "create": TodoSerializer,
        "list": TodoSerializer,
        "partial_update": TodoSerializer,
    }

    def create(self, request, *args, **kwargs):
        user = request.user
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=user)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)