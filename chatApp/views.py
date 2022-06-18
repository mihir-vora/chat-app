from django.shortcuts import render, redirect
from chatApp.models import Room, Message
from django.http import HttpResponse, JsonResponse
# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def room(request, room):
	username = request.GET.get('username')
	print('user name', username)
	room_details = Room.objects.get(name=room)
	print('room_details', room_details)

	message_object = Message.objects.all()

	get_message  = request.GET.get('get_message')

	if get_message != '' and get_message is not None:
		message_object = message_object.filter(user__icontains=get_message)

	context = {
		'username':username,
		'room':room,
		'room_details':room_details,
		'message_object':message_object
	}
	return render(request, 'room.html', context)

def checkview(request):
	room = request.POST['room_name']
	print(room)
	username = request.POST['username']
	print(username)

	# check if the room is already exists or not
	if Room.objects.filter(name=room).exists():
		return redirect('/'+room+'/?username='+username)

	# if room is not exists so create new room
	else:
		# create new chat room
		new_room = Room.objects.create(name=room)
		print(new_room)
		# now creating new room saving in database
		new_room.save()
		return redirect('/'+room+'/?username='+username)

def send(request):
	message = request.POST['message']
	print("Message Take From User : ", message)
	username = request.POST['username']
	room_id = request.POST['room_id']

	# creating message objects
	new_message = Message.objects.create(value=message, user=username, room=room_id)
	new_message.save()
	return HttpResponse("Message Was Successfully Send...")

def getMessages(request, room):
    room_details = Room.objects.get(name=room)


    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


