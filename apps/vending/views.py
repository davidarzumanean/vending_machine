from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from apps.vending.models import Product, User
from apps.vending.serializers import ProductSerializer, UserSerializer


def get_user(username):
    try:
        user = User.objects.get(user_name=username)
    except User.DoesNotExist:
        return Response({'error': f'User with user_name {username} does not exist'}, status=404)

    serializer = UserSerializer(user)
    return serializer.data


class LoginView(APIView):
    def get(self, request: Request) -> Response:
        username = request.query_params.get('user_name', None)

        if not username:
            return Response({'error': 'user_name parameter is missing in the request'}, status=400)

        serializer_data = get_user(username)
        return Response(serializer_data, status=200)


class UserView(APIView):
    def get(self, request: Request, username) -> Response:
        if not username:
            return Response({'error': 'user_name parameter is missing in the request'}, status=400)

        serializer_data = get_user(username)
        return Response(serializer_data, status=200)


class UserBalanceView(APIView):
    def get(self, request: Request, username):
        user = get_user(username)
        return Response({'balance': str(user.balance)}, status=200)

    def patch(self, request: Request, username):
        user = get_user(username)
        amount = request.data['amount']
        user.balance += amount
        user.save()
        return Response({'balance': str(user.balance)}, status=200)


class UserBalanceRefundView(APIView):
    def patch(self, request: Request, username):
        user = get_user(username)
        user.balance = 0
        user.save()
        return Response(status=200)


class ProductsView(APIView):
    def get(self, request: Request) -> Response:
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(data=product_serializer.data)


class BuyProductView(APIView):
    def post(self, request: Request, id) -> Response:
        product = Product.objects.get(id=id)
        username = request.data['username']
        user = get_user(username)

        product.stock -= 1
        user.balance += product.price
        product.save()
        user.save()

        return Response({'balance': str(user.balance), 'stock': str(product.stock)}, status=200)

