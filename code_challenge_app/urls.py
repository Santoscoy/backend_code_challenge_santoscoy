from django.urls import path
from . import views

urlpatterns = [
    path('email/<int:pk>/',views.create_email, name='email')
]