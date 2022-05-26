from django.urls import path

from .views import SelectionView

urlpatterns = [
    path('', SelectionView.as_view(), name="selections"),
    path('<slug:id>/', SelectionView.as_view(), name="selection"),
]