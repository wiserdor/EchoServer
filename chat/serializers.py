from rest_framework import serializers
from chat.models import Message

class MessageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(required=False, allow_blank=True, max_length=255)
    type = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `message` instance, given the validated data.
        """
        return Message.objects.create(**validated_data)