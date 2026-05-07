from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import AccountUserSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class AuthViewSet(viewsets.ViewSet):
    # REGISTER
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = AccountUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(
                {
                    "message": "User created",
                    "username": user.username
                },
                status=201
            )

    # LOGIN (JWT)
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {
                    "error": "Invalid credentials"
                },
                status=401
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            },
            status = 200
        )

    # LOGOUT
    @action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {
                    "message": "Logged out"
                },
                status=205
            )

        except Exception:
            return Response(
                {
                    "error": "Invalid token",
                },
                status=400
            )


