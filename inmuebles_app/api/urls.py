from django.urls import re_path
from inmuebles_app.api import views

urlpatterns = [
    re_path('create', views.create),
    re_path('delete', views.delete),
    re_path('list', views.list),
]
