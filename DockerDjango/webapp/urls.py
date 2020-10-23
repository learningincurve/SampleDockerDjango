from django.urls import path
from .views import FirstView


urlpatterns = [
    path('firstview/',FirstView.as_view()),
    ]