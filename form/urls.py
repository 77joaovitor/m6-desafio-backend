from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("value/", views.sucess, name="upload"),
    path("success/url/", views.sucess, name="process_cnab")
]