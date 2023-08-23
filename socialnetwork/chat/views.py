from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat=chat).order_by('timestamp')
    
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        Message.objects.create(chat=chat, sender=sender, content=content)
    
    return render(request, 'chat/chat.html', {'chat': chat, 'messages': messages})

