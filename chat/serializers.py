from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    channel = serializers.CharField(required=True, max_length=255)
    message = serializers.CharField(required=False, allow_blank=True, max_length=255)
    type = serializers.CharField()
