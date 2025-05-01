import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from users.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chat_with = self.scope['url_route']['kwargs']['username']
        self.room_name = f"chat_{min(self.user.username, self.chat_with)}_{max(self.user.username, self.chat_with)}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data['message']
        recipient = User.objects.get(username=self.chat_with)

        # Save the message to the database
        message = Message.objects.create(
            sender=self.user,
            recipient=recipient,
            content=message_content
        )

        # Send message to WebSocket group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message.content,
                'sender': self.user.username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))
