from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from . import models
from . import encoder

# Create your views here.

def dump(request):
    if "cid" in request.GET:
        return JsonResponse(models.Character.objects.filter(
            id=request.GET["cid"])[0],
            encoder=encoder.CharacterEncoder, safe=False)
    if "rid" in request.GET:
        return JsonResponse(models.Race.objects.filter(
            id=request.GET["rid"])[0],
            encoder=encoder.RaceEncoder, safe=False)
    if "bid" in request.GET:
        return JsonResponse(models.Background.objects.filter(
            id=request.GET["bid"])[0],
            encoder=encoder.BackgroundEncoder, safe=False)
    if "pcid" in request.GET:
        return JsonResponse(models.PlayerClass.objects.filter(
            id=request.GET["pcid"])[0],
            encoder=encoder.PlayerClassEncoder, safe=False)
    return JsonResponse({})

def view_char(request):
    if not "cid" in request.GET:
        return HttpResponse(status=400)
    #return HttpResponse(status=501)
    q = models.Character.objects.filter(id=request.GET["cid"])[0]
    player_classes = models.PlayerClass.objects.all()
    backgrounds = models.Background.objects.all()
    races = models.Race.objects.all()
    levels = [
        (0, 2),
        (300, 2),
        (900, 2),
        (2700, 2),
        (6500, 3),
        (14000, 3),
        (23000, 3),
        (34000, 3),
        (48000, 4),
        (64000, 4),
        (85000, 4),
        (100000, 4),
        (120000, 5),
        (140000, 5),
        (165000, 5),
        (195000, 5),
        (225000, 6),
        (265000, 6),
        (305000, 6),
        (355000, 6),
    ]
    context = {"id": request.GET["cid"], "query": q, "levels": levels,
               "classes": player_classes, "races": races,
               "backgrounds": backgrounds}
    return render(request, "char/view_char.html", context)
