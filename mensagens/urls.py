from django.urls import path
from . import views
from .views import home, delete_mensagem

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:pk>/', delete_mensagem, name='delete_mensagem'),
]
