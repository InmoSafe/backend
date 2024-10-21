from django.urls import re_path
from user_app.api import views

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('testToken', views.testToken),
]
