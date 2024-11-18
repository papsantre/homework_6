from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentListAPIView, PaymentCreateAPIView, UserModelViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', UserModelViewSet)
urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("create/payment/", PaymentCreateAPIView.as_view(), name="create_payment"),
    path('register/', UserCreateAPIView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
] + router.urls
