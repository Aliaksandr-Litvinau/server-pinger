from django.urls import path
from pinger.views import ResponseTimeAPIView, ChartView

urlpatterns = [
    path('responsetime/', ResponseTimeAPIView.as_view(), name='response-time-api'),
    path('chart/', ChartView.as_view(), name='chart'),
]
