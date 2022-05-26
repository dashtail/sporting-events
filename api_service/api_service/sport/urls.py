from django.urls import path

from .views import SportView

urlpatterns = [
    path('', SportView.as_view(), name="sports"),
    path('<slug:id>/', SportView.as_view(), name="sport"),
]