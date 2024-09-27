from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoView, SupportAPIView, AlarmView

app_name = "todo"

router_todo = DefaultRouter()
router_todo.register(prefix="todo", viewset=TodoView)

urlpatterns = [
    path("api/support/<int:todo_id>", SupportAPIView.as_view(), name='support'),
    path("api/alarm/<int:alarm_id>", AlarmView.as_view(), name='alarm'),
    path("api/alarm", AlarmView.as_view(), name='alarm'),
    path("api/", include((router_todo.urls, "restore-api-v1")))
    ]