# Django Chat

Простой чат на Django и WebSocket (Channels), сделанный для практики и демонстрации real-time обмена сообщениями между пользователями.

---

## 🚀 О проекте

- Написан на Django 5.2.1 + Django Channels
- Использует WebSocket для общения в реальном времени
- Подключен Redis в Docker для работы Channels
- Авторизация и регистрация пользователей
- Защита WebSocket авторизацией (только залогиненные могут писать в чат)
- Прокрутка сообщений вниз при новом сообщении
- Bootstrap-оформление интерфейса
- Карточки сообщений разного цвета (свои и чужие)
- Счётчик сообщений в комнатах
- Список всех чатов (Rooms) с переходом в каждую комнату
- Кастомизированный внешний вид (цвета, фон, карточки)
- Возможность создавать новых пользователей через регистрацию
- Logout с редиректом на страницу входа

---

## 📝 Функционал

✅ Реалтайм-чат между пользователями  
✅ Список комнат (Rooms)  
✅ Страницы деталей комнаты с историей сообщений  
✅ Автоматический скролл чата вниз при новом сообщении  
✅ WebSocket соединение через Django Channels  
✅ Подключение Redis через Docker  
✅ Авторизация пользователей  
✅ Регистрация пользователей через форму  
✅ Logout с редиректом на логин  
✅ Защита чатов: писать могут только залогиненные  
✅ Красивый Bootstrap-интерфейс  
✅ Счётчик количества сообщений в каждой комнате  
✅ Разные цвета сообщений (свои и чужие)  
✅ Responsive дизайн (работает и на мобилках)

---

## 📦 Установка

1. Клонируй репозиторий:
https://github.com/SimplRubik/Django_MyChat.git
cd django_chat

2. Создай виртуальное окружение:
   python -m venv venv

3. Активируй виртуальное окружение:
   WINDOWS: venv\Scripts|activate
   macOS/Linux: source venv/bin/activate

4. Установи зависимости:
   pip install -r requirements.txt

---
  Если Ridis не установлен локально, запусти его в Docker:
    docker run -p 6379:6379 redis
---
  Запусти Daphne (ASGI сервер):
    daphne chat_project.asgi:application
    

Simple Chat on Django and WebSocket (Channels) – built for practice and demonstration of real-time messaging between users.

🚀 About the Project
 • Built with Django 5.2.1 + Django Channels
 • Uses WebSocket for real-time communication
 • Redis connected via Docker for Channels support
 • User authentication and registration
 • WebSocket secured by authentication (only logged-in users can write in the chat)
 • Auto-scroll to the bottom on new messages
 • Bootstrap-styled interface
 • Message cards with different colors (own messages vs. others)
 • Message counter in rooms
 • List of all chat rooms with links to enter each room
 • Custom UI styling (colors, background, cards)
 • Ability to create new users via registration form
 • Logout with redirect to login page

📝 Features
✅ Real-time chat between users
✅ List of chat rooms (Rooms)
✅ Room detail pages with message history
✅ Automatic scroll to the bottom on new messages
✅ WebSocket connection via Django Channels
✅ Redis integration via Docker
✅ User authentication
✅ User registration via form
✅ Logout with redirect to login
✅ Chat protection: only logged-in users can send messages
✅ Beautiful Bootstrap interface
✅ Message count in each room
✅ Different colors for messages (yours vs. others)
✅ Responsive design (works on mobile devices too)

📦 Installation
Clone the repository:
git clone https://github.com/SimplRubik/Django_MyChat.git
cd django_chat

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
 • Windows: venv\Scripts\activate
 • macOS/Linux: source venv/bin/activate

Install the dependencies:
pip install -r requirements.txt

If Redis is not installed locally, run it in Docker:
docker run -p 6379:6379 redis

Run Daphne (ASGI server):
daphne chat_project.asgi:application

  

