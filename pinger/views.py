from rest_framework.views import APIView
from rest_framework.response import Response
from pinger.serializers import ResponseTimeSerializer

from django.views.generic import TemplateView
from pinger.models import ResponseTime


class ResponseTimeAPIView(APIView):
    def get(self):
        response_times = ResponseTime.objects.all()
        serializer = ResponseTimeSerializer(response_times, many=True)
        return Response(serializer.data)


class ChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response_times = ResponseTime.objects.all()
        context['response_times'] = response_times
        return context
