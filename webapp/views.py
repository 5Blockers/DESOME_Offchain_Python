from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from webapp.final import find_plagiarism

from . models import ImageChecker
from . serializers import ImageCheckerSerializer

# Create your views here.

@csrf_exempt
def imageCheckerApi(request):
    if request.method=='POST':
        images = ImageChecker.objects.all()
        image_data = JSONParser().parse(request)
        link1, link2 = image_data[0], image_data[1]
        checker = find_plagiarism(ImageChecker, link1, link2)
        image_serializer=ImageCheckerSerializer(data=checker)
        if image_serializer.is_valid():
            return JsonResponse(True)
        return JsonResponse(False)