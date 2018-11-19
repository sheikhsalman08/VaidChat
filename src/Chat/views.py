from django.shortcuts import render
from django.http import HttpResponse
from .models import Msg
from django.utils import timezone
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponse('Please Log In First')

	if request.method == 'POST':
		try:
			txt = request.POST['txt']
			msg = Msg()
			msg.txt = txt
			msg.sender = request.user
			msg.save()
		except:
			return HttpResponse('Not a Valid Entity')

	context = {
		'msgs' : Msg.objects.all().order_by('-id'),
		'current_user': mark_safe(json.dumps(request.user.username))
	}

	return render(request, 'chat/index.html', context)
	# chat/views.py
# 	return render(request, 'chat/index.html', {})

# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })