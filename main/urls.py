from django.urls import path

from .views import MainAPI

urlpatterns = [
    path('', MainAPI.as_view()),
]
