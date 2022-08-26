from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import ImageChecker
from . serializers import ImageCheckerSerializer
from webapp.final import find_plagiarism
# Create your views here.

class ImageProcessing(APIView):
    def post(self, request):
        imageChecker = find_plagiarism(ImageChecker.__new__, request.query_params['check_image_link'], request.query_params['image_link'])
        serializer = ImageCheckerSerializer(imageChecker)
        return Response(serializer.data)
    