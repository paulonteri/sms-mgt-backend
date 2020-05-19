from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class RegisterAPI(generics.GenericAPIView):
    """
    Register API
    """
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # send back any errors
        serializer.is_valid(raise_exception=True)
        # save user
        user = serializer.save()
        # send response back
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # create and send back token
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    """
    Login API
    """
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny,]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # send back any errors
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        # send response(RF) back
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            # create and send back token
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    """
    Get User API
    """
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        # get user using the token in isAuthenticated
        return self.request.user
