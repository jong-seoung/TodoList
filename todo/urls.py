from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoView

app_name = "todo"

router_todo = DefaultRouter()
router_todo.register(prefix="todo", viewset=TodoView)

urlpatterns = [path("api/", include((router_todo.urls, "restore-api-v1")))]