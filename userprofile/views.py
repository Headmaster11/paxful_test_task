from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password=data['password'],
    )
    token = Token.objects.create(user=user)
    return Response(token.key, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    if user:
        token, _ = Token.objects.get_or_create(user=User.objects)
        return Response(token)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
