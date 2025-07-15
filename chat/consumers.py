import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        print("Scope user:", user)

        if not user.is_authenticated:
            # Закрываем соединение для анонимов
            await self.close()
            return

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # добавляем пользователя в группу
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Убираем пользователя из группы при отключении
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        user = self.scope["user"]

        if not user.is_authenticated:
            # Закрываем соединение, если кто-то лезет без логина
            await self.close()
            return

        data = json.loads(text_data)
        message = data['message']

        username = user.username

        # сохраняем сообщение в базу
        await self.save_message(user, message)

        # рассылаем сообщение всем в группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
        }))

    @database_sync_to_async
    def save_message(self, user, message):
        try:
            room = Room.objects.get(name=self.room_name)
            Message.objects.create(room=room, user=user, content=message)
        except Room.DoesNotExist:
            print(f"Room {self.room_name} does not exist!")