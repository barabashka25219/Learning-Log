from django.urls import path, include
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('remove_topic/<int:topic_id>', views.remove_topic, name='remove_topic'),
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('remove_entry/<int:entry_id>', views.remove_entry, name='remove_entry'),
]
