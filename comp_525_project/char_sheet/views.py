from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from . import models
from . import encoder

# Create your views here.

def dump(request):
    """
    JSON database dump view

    GET parameters (only accepts one):
    cid: id in the database of the character to dump
    rid: id in the database of the race to dump
    bid: id in the database of the background to dump
    pcid: id in the database of the class to dump
    akid: id in the database of the attack to dump
    arid: id in the database of the armor to dump
    iid: id in the database of the item to dump

    Returns:
    JSON of the requested database row
    Empty JSON if no GET argument
    OR
    HTTP status 403 (Forbidden) with cid if the user doesn't have permission.
    The user has permission either if they own the character or they are in
    the can_view field.
    """
    if "cid" in request.GET:
        if not (request.user in models.Character.objects.filter(
                        id=data["cid"])[0].can_view or
                    request.user == models.Character.objects.filter(
                        id=data["cid"])[0].owner):
            return JsonResponse(
                models.Character.objects.filter(id=request.GET["cid"])[0],
                encoder=encoder.CharacterEncoder,
                safe=False)
        else:
            return HttpResponse(status=403)
    if "rid" in request.GET:
        return JsonResponse(
            models.Race.objects.filter(id=request.GET["rid"])[0],
            encoder=encoder.RaceEncoder,
            safe=False)
    if "bid" in request.GET:
        return JsonResponse(
            models.Background.objects.filter(id=request.GET["bid"])[0],
            encoder=encoder.BackgroundEncoder,
            safe=False)
    if "pcid" in request.GET:
        return JsonResponse(
            models.PlayerClass.objects.filter(id=request.GET["pcid"])[0],
            encoder=encoder.PlayerClassEncoder,
            safe=False)
    if "akid" in request.GET:
        return JsonResponse(
            models.Attack.objects.filter(id=request.GET["akid"])[0],
            encoder=encoder.AttackEncoder,
            safe=False)
    if "arid" in request.GET:
        return JsonResponse(
            models.Armor.objects.filter(id=request.GET["arid"])[0],
            encoder=encoder.ArmorEncoder,
            safe=False)
    if "iid" in request.GET:
        return JsonResponse(
            models.Item.objects.filter(id=request.GET["iid"])[0],
            encoder=encoder.ItemEncoder,
            safe=False)
    return JsonResponse({})

def view_char(request):
    """
    Displays character information in a table

    GET parameters:
    cid: id in the database of the character to display

    returns:
    HTTP status 400 on bad request
    render of the file at char/view_char.html with the context:
        id: cid passed from GET params
        query: the character's row in the database
        levels: a list of tuples in the form (required experience, proficiency
                bonus)
        classes: all classes in the database
        races: all races in the database
        backgrounds: all backgrounds in the database
        level: the character's current level
    """
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

    level = 0

    for level_pair in levels:
        if q.experience > level_pair[0]:
            level += 1

    context = {"id": request.GET["cid"], "query": q, "levels": levels,
               "classes": player_classes, "races": races,
               "backgrounds": backgrounds, "level": level}
    return render(request, "char/view_char.html", context)

def update(request):
    """
    Updates information to the database
    The request should contain JSON data in the same form as what is returned
    by dump, with an additional key "cid" to indicate the id of the character
    in the database being updated.

    Right now, there is no good reason to update any other values in the
    database.

    The ID is the only mandatory field.

    Only one ID can be used at once.
    An ID of zero will be interpreted as inserting into the table.

    This can be sent either as the sole contents of the request body, or in
    a key named "data".

    POST Parameters:
    data: JSON data containing the request OR
    none: in which case the JSON data must be only data in the request.

    Returns:
    HTTP 400 (Bad Request) on malformed request
    HTTP 403 (Forbidden) if the user does not have adequate permission
    HTTP 200 (OK) on success

    On success, the item's id will be in the body of the response
    """

    if len(request.POST) > 0:
        if not "data" in request.POST:
            return HttpResponse(status=400)
        data = json.loads(request.POST["data"])
    else:
        data = json.loads(request.body.decode("utf-8"))


    if "cid" in data:
        data["cid"] = int(data["cid"])
        if data["cid"] == 0:
            new_item = models.Character()
        else:
            new_item = models.Character.objects.filter(id=data["cid"])[0]
            
        # this interface only looks for cids currently, and it likely will NOT
        # be expanded to cover other database tables, so we're only testing for
        # authentication here.
        # Witness the drawback to object-oriented programming
        if data["cid"] != 0:
            if not (request.user in
                    models.Character.objects.filter(
                        id=data["cid"])[0].can_edit or
                    request.user == models.Character.objects.filter(
                        id=data["cid"])[0].owner):
                return HttpResponse(status=403)
    # I don't think there's any reason to update this data from here
    # elif "rid" in data:
    #     data["rid"] = int(data["rid"])
    #     if data["rid"] == 0:
    #         new_item = models.Race()
    #     else:
    #         new_item = models.Race.objects.filter(id=data["rid"])[0]
    # elif "bid" in data:
    #     data["bid"] = int(data["bid"])
    #     if data["bid"] == 0:
    #         new_item = models.Background()
    #     else:
    #         new_item = models.Background.objects.filter(id=data["bid"])[0]
    # elif "pcid" in data:
    #     data["pcid"] = int(data["pcid"])
    #     if data["pcid"] == 0:
    #         new_item = models.PlayerClass()
    #     else:
    #         new_item = models.PlayerClass.objects.filter(id=data["pcid"])[0]
    else:
        print("DEBUG: invalid ID")
        return HttpResponse(status=400)

    for key in data:
        if not hasattr(new_item, key):
            if key in ["cid", "rid", "bid", "pcid"]:
                continue
            return HttpResponse(status=400)
        if key == "background":
            new_item.background = models.Background.objects.filter(id=data[key])[0]
        elif key == "race":
            new_item.race = models.Race.objects.filter(id=data[key])[0]
        elif key == "player_class":
            new_item.player_class = models.PlayerClass.objects.filter(id=data[key])[0]
        else:
            setattr(new_item, key, data[key])
    new_item.save()
    return HttpResponse(new_item.id, status=200)

def api(request):
    """
    Calls the appropriate function to handle API calls based on HTTP method.
    For GET calls, calls dump()
    For POST calls, calls update()
    If any other method is used, return HTTP status 405 (method not allowed).
    """
    if request.method == "GET":
        dump(request)
    else if request.method == "POST":
        update(request)
    else:
        return HttpResponse(status=405)

def test_post(request):
    return render(request, "char/testpost.html", {})
