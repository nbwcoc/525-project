from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^api/', views.api, name="api"),
    url(r'^view_char/', views.view_char, name='view_char'),
    url(r'^testpost/', views.test_post, name="test_post")
]
