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

class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer
    class Meta:
        model = Answer
        fields = '__all__'

class UserTestSerializer(serializers.ModelSerializer):
    test = TestSerializer
    class Meta:
        model = UserTest
        fields = '__all__'
