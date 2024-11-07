from rest_framework import serializers
from chart.charts.models import ChartData

class ChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartData
        fields = ['dateTime', 'value']



