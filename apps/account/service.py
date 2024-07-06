from datetime import datetime,timezone
from apps.account.models import Account
from rest_framework_simplejwt.tokens import RefreshToken
from api.account.serializers import UserDetailSerializer
from django.conf import settings


def get_token_for_user(user):
    try:
        tokens = RefreshToken.for_user(user)
        return{
            'refresh_token' : tokens,
            'access_token' : tokens.access_token
        }
    except:
        return 1003

def login_eu(username,password):
    try:
        username = username.lower()
        user = Account.objects.get(username = username)
        if not user:
            return 1000
        if not user.check_password(password):
            return 1002
        jwt_response = get_token_for_user(user)
        if not jwt_response:
            return 1002
        else:
            user_detail_serializer = UserDetailSerializer(user)
            #add prefix to the generated jwt token values
            bearer_token = {key: f"{settings.AUTH_PREFIX} {val}" for key, val in jwt_response.items()}
            user.last_login = datetime.now().replace(tzinfo=timezone.utc)
            user.save()
            return {
                        'token': bearer_token,
                        'data' : user_detail_serializer.data,
                    }
    except:
        return 1004
        