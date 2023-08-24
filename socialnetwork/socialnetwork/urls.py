from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views import ChatViewSet, MessageViewSet
from users.views import ProfileViewSet

router = DefaultRouter()
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'users', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls