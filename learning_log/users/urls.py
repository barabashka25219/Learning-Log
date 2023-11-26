from django.urls import path, include

app_name = 'users'
url_patterns = [
    path('', include('django.contrib.auth.urls')),
]