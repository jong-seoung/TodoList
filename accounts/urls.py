from django.urls import path
from .views import LoginView, LogoutView, SignupView, FollowView, HealthCheckView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("health_check", HealthCheckView.as_view()),
    path("follow/<int:receive_user>", FollowView.as_view(), name="follow"),
]