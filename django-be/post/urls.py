from django.urls import path
from . import api

urlpatterns = [
    path('/api/post/', api.post_list, name='post_list'),
]