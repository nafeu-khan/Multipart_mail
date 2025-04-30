### urls.py
from django.urls import path
from .views import SelectionEmailView

urlpatterns = [
    path("send-email/", SelectionEmailView.as_view(), name="send-selection-email")
]