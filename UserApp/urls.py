
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from UserApp.views import  FinancialAccount as FinancialAccountViewSet, UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'user/payment',FinancialAccountViewSet,basename='inancial')


urlpatterns = [
    path(f'', include(router.urls)),
    path(f'auth/', ObtainAuthToken.as_view(),name='auth'),
]
