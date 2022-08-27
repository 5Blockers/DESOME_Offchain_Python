from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CheckApp.final import find_plagiarism
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json

from . models import ImageChecker
from .serializers import ImageChecker, ImageCheckerSerializer

# Create your views here.

@csrf_exempt
# @api_view()
# @permission_classes([AllowAny])
def imageCheckerApi(request):
    if request.method=='POST':
        # images = ImageChecker.objects.all()
        image_data = JSONParser().parse(request)
        print(image_data[0]['link1'])
        checker = find_plagiarism(ImageChecker(), image_data[0]['link1'], image_data[1]['link2'])
        image_serializer=ImageCheckerSerializer(data=checker,many=True)
        if image_serializer.is_valid():
            return JsonResponse(True,safe=False)
        return JsonResponse(False,safe=False)
    # elif request.method=='GET':
    #     return JsonResponse("Hello",safe=False)