from rest_framework import serializers
from . models import ImageChecker

class ImageCheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageChecker
    fields = '__all__'