
from django.urls import path
from hello_world import views
urlpatterns = [
    path('', views.helloWorld, name='helloworld'),
    path('bonjour/', views.bonjour, name='bonjour'),
]