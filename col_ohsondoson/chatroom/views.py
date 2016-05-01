from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def chatroom_view(request):
    rulname = request.POST.get('url')
    print(rulname)
    req = requests.get(rulname)
    return HttpResponse(req.text)


def room_view(request):
     return render(
        request,
        'createroom.html',
    )
