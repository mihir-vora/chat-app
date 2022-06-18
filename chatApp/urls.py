from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	# dynamic path / print the room name and username in url
	path('<str:room>/', views.room, name="room"),
	# checking the chat room exists or not if not chat room create and enter the chat room
	# if chat room exist you directly chat with your partner
	path('checkview', views.checkview, name="checkview"),
	# sending for data
	path('send', views.send, name="send"),
	# getting the existing message
	path('getMessages/<str:room>/', views.getMessages,name="getMessages"),
]