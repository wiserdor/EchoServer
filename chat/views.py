from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from channels.layers import get_channel_layer


@api_view(['POST'])
def echo(request):
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        #send message to itself

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def broadcast(request):
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        #send message to everyone
        channel_layer = get_channel_layer()
        channel_layer
        for chat_name in chats:
            await channel_layer.group_send(
                chat_name,
                {"type": "chat.system_message", "text": announcement_text},
            )


        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
