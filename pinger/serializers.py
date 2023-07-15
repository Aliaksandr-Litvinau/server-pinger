from rest_framework import serializers
from pinger.models import ResponseTime


class ResponseTimeSerializer(serializers.ModelSerializer):
    time_hour = serializers.SerializerMethodField()

    class Meta:
        model = ResponseTime
        fields = ['domain', 'time', 'response_time', 'time_hour']

    def get_time_hour(self, obj):
        return obj.time.hour if obj.time else None
