from django.urls import path
from .views import download_excel


urlpatterns = [
    path('export-data/', download_excel, name='export-excel')
]