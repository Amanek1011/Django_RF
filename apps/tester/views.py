from django.http import HttpResponse
from rest_framework import status, generics, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from apps.tester.models import Test, Question, Answer, UserTest
from apps.tester.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, UserTestSerializer


# Create your views here.
@api_view(['GET'])
def hello(request):
    return HttpResponse('Hello, world!')

# model Test
class TestListApiView(APIView):
    def get(self,request):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

class TestDetailApiView(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestListAPIView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]


# model Question
class QuestionDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Exception:
            return None

    def get(self, request, pk):
        question = self.get_object(pk)
        if question is None:
            return Response({'message': 'Question not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionListApiView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# model Answer
class AnswerDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Exception:
            return None

    def get(self, request, pk):
        answer = self.get_object(pk)
        if answer is None:
            return Response({'message': 'Answer not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

class AnswerDetailAPIView(generics.RetrieveAPIView):
       queryset = Answer.objects.all()
       serializer_class = AnswerSerializer

class AnswerListApiView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


# model UserTest

class UserTestDetailApiView(APIView):
    def get_object(self,pk):
        try:
            return UserTest.objects.get(pk=pk)
        except Exception:
            return None

    def get(self, request, pk):
        user_test = self.get_object(pk)
        if user_test is None:
            return Response({'message': 'UserTest not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserTestSerializer
        return Response(serializer.data)

class UserTestDetailAPIView(generics.RetrieveAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer

class UserTestListApiView(generics.ListAPIView):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer

class UserTestViewSet(viewsets.ModelViewSet):
    queryset = UserTest.objects.all()
    serializer_class = UserTestSerializer