from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dump/', views.dump, name="dump"),
    url(r'view_char/', views.view_char, name='view_char'),
]
