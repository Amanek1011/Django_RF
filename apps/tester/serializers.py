from rest_framework import serializers

from .models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    test = TestSerializer
    class Meta:
        model = Question
        fields = '__all__'