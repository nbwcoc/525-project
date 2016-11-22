from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^dump/', views.dump, name="dump"),
    url(r'^view_char/', views.view_char, name='view_char'),
    url(r'^update/', views.update, name="update"),
    url(r'^testpost/', views.test_post, name="test_post")
]
