# accounts/views.py
from django.shortcuts import get_object_or_404
from accounts.serializers import LoginSerializer, SignupSerializer
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User, Follow
from todo.models import Alarm
from core.loggings import log_db_url



class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        log_db_url()
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            auth_login(request, user)
            return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        auth_logout(request)
        return Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
    

class FollowView(APIView):
    def post(self, request, receive_user):
        send_user = request.user
        receive_user = get_object_or_404(User, id=receive_user)

        follow_instance = Follow.objects.filter(send_user=send_user, receive_user=receive_user)

        if follow_instance:
            follow_instance.delete()
            return Response({"detail": "언팔"}, status=status.HTTP_200_OK)
        else:
            Follow.objects.create(send_user=send_user, receive_user=receive_user)

            Alarm.objects.create(
                sender=send_user,
                receiver=receive_user,
                type='follow',
                content=f'{send_user.profile.nickname}님이 당신을 팔로우합니다.'
            )

            return Response({"detail": "팔로우"}, status=status.HTTP_201_CREATED)


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"detail":"서버 작동 중"},status=status.HTTP_200_OK)
