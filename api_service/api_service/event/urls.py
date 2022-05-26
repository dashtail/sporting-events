from django.urls import path

from .views import EventView

urlpatterns = [
    path('', EventView.as_view(), name="events"),
    path('<slug:id>/', EventView.as_view(), name="event"),
]