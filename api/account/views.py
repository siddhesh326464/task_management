from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from api.account import serializers as account_serializer
from drf_yasg.utils import swagger_auto_schema
from utils.constant import API_AUTH
from apps.account import service as account_service
from utils.common import dispatch_response

class LoginEU(generics.GenericAPIView):
    """
    Login view
    """
    allowed_methods = ("POST",)
    serializer_class = account_serializer.LoginEUSerializer

    @swagger_auto_schema(
        operation_description="\
            <b>Username: </b> <a style='text-decoration:none !important; color:black; pointer-events:none;'>admin@addnectar.com </a> <br><br> \
            <b>Pasword: </b> Add@2023",
        
        tags=[API_AUTH]
    )
    def post(self,request):
        serializer = account_serializer.LoginEUSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        res = account_service.login_eu(data['username'],data['password'])
        return dispatch_response(res)