from django.urls import path
from .views import BookAPIView

urlpatterns = [
    # Example:
    path('', BookAPIView.as_view()),
]