from dataclasses import field
from rest_framework import serializers
from .models import ImageChecker

class ImageCheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageChecker
        fields = ('min_dist','flag','result_link')