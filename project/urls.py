from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telegram-webhook', views.telegram_webhook, name='telegram_webhook'),
]
