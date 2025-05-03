import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Notification
from users.models import User
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chat_with = self.scope['url_route']['kwargs']['username']
        self.room_name = f"chat_{min(self.user.username, self.chat_with)}_{max(self.user.username, self.chat_with)}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    @database_sync_to_async
    def create_message_and_notification(self, sender, recipient, content):
        message = Message.objects.create(
            sender=sender,
            recipient=recipient,
            content=content
        )
        Notification.objects.create(
            recipient=recipient,
            sender=sender,
            message=message
        )
        return message

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data['message']
        recipient = await database_sync_to_async(User.objects.get)(username=self.chat_with)

        # Create message and notification
        message = await self.create_message_and_notification(
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

        # Send notification to recipient's notification channel
        await self.channel_layer.group_send(
            f"notifications_{recipient.username}",
            {
                'type': 'notification_message',
                'message': message.content,
                'sender': self.user.username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))

    async def notification_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
            'sender': event['sender'],
        }))
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Notification
from users.models import User
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chat_with = self.scope['url_route']['kwargs']['username']
        self.room_name = f"chat_{min(self.user.username, self.chat_with)}_{max(self.user.username, self.chat_with)}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    @database_sync_to_async
    def create_message_and_notification(self, sender, recipient, content):
        message = Message.objects.create(
            sender=sender,
            recipient=recipient,
            content=content
        )
        Notification.objects.create(
            recipient=recipient,
            sender=sender,
            message=message
        )
        return message

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data['message']
        recipient = await database_sync_to_async(User.objects.get)(username=self.chat_with)

        # Create message and notification
        message = await self.create_message_and_notification(
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

        # Send notification to recipient's notification channel
        await self.channel_layer.group_send(
            f"notifications_{recipient.username}",
            {
                'type': 'notification_message',
                'message': message.content,
                'sender': self.user.username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
        }))

    async def notification_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
            'sender': event['sender'],
        }))

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.notification_group = f"notifications_{self.user.username}"
        await self.channel_layer.group_add(self.notification_group, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.notification_group, self.channel_name)

    async def notification_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
            'sender': event['sender'],
        }))