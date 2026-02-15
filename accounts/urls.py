from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('homepage1/', views.homepage1, name='homepage1'),
    path('homepage2/', views.homepage2, name='homepage2'),
]