from django.urls import path
from api.account import views as api_account_view

urlpatterns = [
    path('login/',api_account_view.LoginEU.as_view(), name='auth_login')

]