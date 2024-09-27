from django.urls import path
from .views import LoginView, LogoutView, SignupView, FollowView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("follow/<int:receive_user>", FollowView.as_view(), name="follow"),
]