from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from .serializers import MessageSerializer
from channels.layers import get_channel_layer


class EchoView(GenericViewSet):

    async def post(self, request, pk=None):
        if request.method == 'POST':
            serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            channel_layer = get_channel_layer()
            await channel_layer.send(serializer.channel, {
                "message": serializer.message,
            })
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BroadcastView(GenericViewSet):

    async def post(self, request, pk=None):
        if request.method == 'POST':
            serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # send message to everyone
            channel_layer = get_channel_layer()
            await channel_layer.group_send('chat', {
                "message": serializer.message,
            })

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
