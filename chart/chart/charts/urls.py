from django.urls import  path
from chart.charts.views import  line_chart_view

app_name = "charts"
urlpatterns = [
    path('line-chart/', line_chart_view, name='line-chart'),
]
