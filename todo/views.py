from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from core.mixins import ActionBasedViewSetMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView

from todo.models import Todo,SupportTodo
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class SupportAPIView(APIView):
    def post(self, request, todo_id):
        user = request.user
        support_todo = SupportTodo.objects.filter(todo_id=todo_id, send_user=user).first()

        if support_todo:
            if support_todo.is_support == True:
                support_todo.is_support = False
            else:
                support_todo.is_support = True
            support_todo.save()
            return Response({"detail": f"지원 상태가 {support_todo.is_support}로 업데이트되었습니다."}, status=status.HTTP_200_OK)
        else:
            todo_instance = get_object_or_404(Todo, id=todo_id) 
            SupportTodo.objects.create(todo=todo_instance, send_user=user, is_support=True)
            return Response({"detail": "SupportTodo가 생성되었습니다."}, status=status.HTTP_201_CREATED)