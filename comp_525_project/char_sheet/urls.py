from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dump/', views.dump, name="dump"),
]
