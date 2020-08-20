from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_tracking.mixins import LoggingMixin


class JWTTokenObtainPairView(LoggingMixin, TokenObtainPairView):
    pass


class JWTTokenRefreshView(LoggingMixin, TokenRefreshView):
    pass
