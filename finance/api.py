from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.services.africastalking import get_balance


class GetBalanceAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        try:
            bal = get_balance()
        except Exception as error:
            raise APIException(error)
        else:
            return Response({"balance": bal})
