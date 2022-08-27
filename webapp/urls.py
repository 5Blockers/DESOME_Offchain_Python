from django.urls import re_path
from webapp import views



urlpatterns = [
    re_path(r'^image-check$',views.imageCheckerApi)
]