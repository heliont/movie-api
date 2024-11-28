from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    # Geração de token de acesso para usuário
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Renova o token de acesso
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Verifica o token de acesso é inválido ou expirado
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]