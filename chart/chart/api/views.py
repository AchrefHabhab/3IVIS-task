from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ChartDataSerializer
from chart.charts.models import ChartData

class ChartDataAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = ChartData.objects.order_by('dateTime')
        serializer = ChartDataSerializer(data, many=True)
        return Response(serializer.data)
