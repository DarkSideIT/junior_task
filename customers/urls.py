from django.urls import path
from .views import OrderRobotView, update_robot_availability_api


urlpatterns = [
    path('order-robot/', OrderRobotView.as_view(), name='create-robot-order'),
    path('<int:robot_id>/update-availability/', update_robot_availability_api, name='update')
]