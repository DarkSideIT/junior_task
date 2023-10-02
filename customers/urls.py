from django.urls import path
from .views import OrderRobotView


urlpatterns = [
    path('order-robot/', OrderRobotView.as_view(), name='create-robot-order')
]