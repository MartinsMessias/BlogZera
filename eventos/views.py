from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.timezone import localdate
from .models import *
from django.core.paginator import Paginator, InvalidPage

@login_required
def page_eventos(request):
    events = Evento.objects.all()
    total = Evento.objects.count()
    return render(request, "eventos/eventos.html", {'events': events, 'total':total})
