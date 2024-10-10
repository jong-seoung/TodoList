from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.views import APIView

from todo.models import Todo,SupportTodo, Alarm
from todo.serializers import TodoSerializer, AlarmSeralizer
from core.mixins import ActionBasedViewSetMixin
from core.permissions import IsAuthorOrReadonly, IsAuthenticatedAndOnwerOrReadonly
from core.loggings import log_db_url


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
    permission_classes = [IsAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


class SupportAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, todo_id):
        user = request.user
        support_todo = SupportTodo.objects.filter(todo_id=todo_id, send_user=user).first()

        if support_todo:
            support_todo.is_support = not support_todo.is_support
            support_todo.save()
            return Response({"detail": f"지원 상태가 {support_todo.is_support}로 업데이트되었습니다."}, status=status.HTTP_200_OK)
        else:
            todo_instance = get_object_or_404(Todo, id=todo_id) 
            SupportTodo.objects.create(todo=todo_instance, send_user=user, is_support=True)

            Alarm.objects.create(
                sender=user,
                receiver=todo_instance.author,
                type='support',
                content=f'{user.profile.nickname}님이 당신의 투두를 응원합니다.'
            )

            return Response({"detail": "SupportTodo가 생성되었습니다."}, status=status.HTTP_201_CREATED)
        

class AlarmView(APIView):
    permission_classes = [IsAuthenticatedAndOnwerOrReadonly]

    def get(self, request):
        log_db_url()
        user = request.user
        alarm = Alarm.objects.filter(receiver=user, is_read=False).order_by('-created_at')
        serializer = AlarmSeralizer(alarm, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, alarm_id):
        alarm = get_object_or_404(Alarm, id=alarm_id, receiver=request.user)
        alarm.is_read=True
        alarm.save()
        return Response({"detail": f"{alarm.content}를 읽음 처리"}, status=status.HTTP_200_OK)
