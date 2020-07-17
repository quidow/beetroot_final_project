from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from .views import CreateUserView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signup/', CreateUserView.as_view(), name='signup'),  # for frontend froject
]
