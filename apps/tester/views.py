from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from apps.tester.models import Test, Question
from apps.tester.serializers import TestSerializer, QuestionSerializer


# Create your views here.
@api_view(['GET'])
def hello(request):
    return HttpResponse('Hello, world!')

class TestListApiView(APIView):
    def get(self,request):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

class QuestionDetailApiView(APIView):
    def get_object(self,pk):
        try:
            return Question.objects.get(pk=pk)
        except Exception:
            return None

    def get(self,request,pk):
        question = self.get_object(pk)
        if question is None:
            return Response({'message': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
