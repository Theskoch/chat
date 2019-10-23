from django.shortcuts import render
from django.utils import timezone
from .models import chats

def chats_list(request):
    chats_l = chats.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'chat/chats_list.html', {'chats_l':chats_l})