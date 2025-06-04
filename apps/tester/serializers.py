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

class AnswerSubmissionSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()

class TestSubmissionSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=300)
    answers = AnswerSubmissionSerializer(many=True)
