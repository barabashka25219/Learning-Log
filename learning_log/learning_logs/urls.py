from django.urls import path, include
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
]
