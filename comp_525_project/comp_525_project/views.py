"""
auth
"""

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def logon(request):
    if request.method != "POST":
        return HttpResponse(status=400)
    try:
        user = authenticate(request.POST["username"], request.POST["password"])
    except PermissionDenied:
        return HttpResponse(status=403)
    if user is None:
        return HttpResponse(status=403)
    else:
        login(request, user)
        return HttpResponse(user.id, status=200)
