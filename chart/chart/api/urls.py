from django.urls import path
from .views import ChartDataAPIView
app_name = "api"

urlpatterns = [
    path('line-chart-data/', ChartDataAPIView.as_view(), name='line-chart-data'),
]
