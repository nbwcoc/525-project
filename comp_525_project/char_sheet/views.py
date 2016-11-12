from django.shortcuts import render
from django.http import JsonResponse
from . import models
from . import encoder

# Create your views here.

def dump(request):
    if not "cid" in request.GET:
        return JsonResponse({})
    return JsonResponse(models.Character.objects.filter(id=request.GET["cid"])[0],
                        encoder=encoder.CharacterEncoder, safe=False)

