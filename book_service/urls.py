from typing import List, Any
from django.urls import path, include
from django.contrib import admin

from book_service.views import (
    create_user, user_list, backend_logout
)

urlpatterns: List[Any] = [
    path(r'create_user', create_user, name='create_user'),
    path(r'user_list', user_list, name='user_list'),
    path(r'backend_logout', backend_logout, name='backend_logout'),
]

