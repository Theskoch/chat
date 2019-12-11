from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import chats, masege, test_json     
from .forms import masegeForm
from django.shortcuts import redirect

import json
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model

from django.http import HttpResponse

from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

import logging

logger = logging.getLogger(__name__)

# logger.error('Something went wrong!')

filter_time='-date'

def chats_list(request):
    chats_l = chats.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'chat/chats_list.html', {'chats_l':chats_l})

def masege_ls(request, name_chat):
    name = name_chat
    if request.method == "POST":
        form = masegeForm(request.POST)
        if form.is_valid():
            masege_s = form.save(commit=False)
            masege_s.hash = "#" + name
            masege_s.author = request.user
            masege_s.fazer = 0
            masege_s.name_chats = name
            masege_s.save()
            form = masegeForm()
            maseges = masege.objects.filter(name_chats__contains = name,date__lte=timezone.now()).order_by('date')
            return render(request, 'chat/masege.html', {'maseges': maseges, 'form': form})
    else:
        maseges = masege.objects.filter(name_chats__contains = name_chat,date__lte=timezone.now()).order_by('date')
        form = masegeForm()
    return render(request, 'chat/masege.html', {'maseges': maseges, 'form': form})

class chat_test_class():
    def chats_test(request):
        name = "FreeNet"
        maseges = masege.objects.filter(name_chats__contains = name,date__lte=timezone.now()).order_by('date')
        nan = "nan"
        maseges_f = masege.objects.filter(name_chats__contains = name,date__lte=timezone.now()).order_by('date')
        

        return render(request, 'chat/test_chat.html',{'maseges_f':maseges_f,'maseges':maseges,'nan':nan})


def test_json_fanck(request):
    # name = "FreeNet"
    # maseges = masege.objects.filter(name_chats__contains = name,date__lte=timezone.now()).order_by('date')
    # dump = json.dumps(maseges)

    data = [{
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    },{
        'name': 'Vitoria',
        'location': 'Finland',
        'is_active': True,
        'count': 23}]
    
    dump2 = json.dumps(data)
    logger.error("goood hueta")
    chat = chats.objects.all()

    name = 'FreeNet'
    mas = masege.objects.all().values('id', 'author', 'text', 'fazer')
    mas4 = json.dumps([dict(item) for item in mas])

    #data_ready_for_json = list( ConventionCard.objects.filter(ownerUser = user).values('fileName','id') )
    
    # suka pashet vau
    sort = test_json.objects.all().values('id', 'author', 'name_chats', 'hash')
    mas2 = json.dumps([dict(item) for item in sort])
    
    logger.error(test_json)
    logger.error("GG")
    mas3 = mas2
    dump = mas4
    print (mas3)

    from django.core import serializers
    # dump = serializers.serialize("json", [mas])

    logger.error("mas sakses")
    
    #logger.error(dump)
    

    # dump2 = json.dumps(mas).first().values()
    # json_j=json.dumps(masege.objects.all())
    # logger.error(json_j)
    # dump = masege.objects.all()
    # return HttpResponse(dump, content_type='application/json')
    return render(request, 'chat/test_json.html',{'dump':dump, 'mas': mas})
    #return render(request, 'chat/test_json.html', {'maseges_json':maseges_json})