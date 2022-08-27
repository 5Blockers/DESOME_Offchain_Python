from django.urls import re_path
from CheckApp import views



urlpatterns = [
    re_path(r'^image-check$',views.imageCheckerApi)
]