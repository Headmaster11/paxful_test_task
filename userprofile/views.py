from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q, Sum
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from transactions.models import Transaction


@api_view(['POST'])
def register(request):
    data = request.data
    if User.objects.filter(Q(email=data['email']) | Q(username=data['username'])).first():
        return Response({'error': 'already exists'}, status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
    )
    token = Token.objects.create(user=user)
    return Response({'token': token.key}, status.HTTP_201_CREATED)


@api_view(['POST'])
def login(request):
    data = request.data
    if not User.objects.get(username=data['username']):
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = authenticate(username=data['username'], password=data['password'])
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def statistics(request):
    token = request.META['HTTP_AUTHORIZATION']
    if token == settings.ADMIN_TOKEN:
        transactions = Transaction.objects.all()
        total_transactions = transactions.count()
        platform_profit = transactions.aggregate(Sum('platform_profit'))
        return Response(
            {
                'total_transactions': total_transactions,
                'platform_profit in BTS': platform_profit['platform_profit__sum']
            })
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
