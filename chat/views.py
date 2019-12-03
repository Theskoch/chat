from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import chats, masege 
from .forms import masegeForm
from django.shortcuts import redirect

from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

# import logging

# logger = logging.getLogger(__name__)

# logger.error('Something went wrong!')

filter_time='-date'

def chats_list(request):
    chats_l = chats.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'chat/chats_list.html', {'chats_l':chats_l})

def masege_ls(request, name_chat):
    if request.method == "POST":
        form = masegeForm(request.POST)
        if form.is_valid():
            masege_s = form.save(commit=False)
            masege_s.hash = "#" + name
            masege_s.author = request.user
            masege_s.fazer = "nan"
            masege_s.name_chats = name
            masege_s.save()
            form = masegeForm()
            maseges = masege.objects.filter(name_chats__contains = name,date__lte=timezone.now()).order_by('date')
            return render(request, 'chat/masege.html', {'maseges': maseges, 'form': form})
    else:
        maseges = masege.objects.filter(name_chats__contains = name_chat,date__lte=timezone.now()).order_by('date')
        form = masegeForm()
    return render(request, 'chat/masege.html', {'maseges': maseges, 'form': form})

