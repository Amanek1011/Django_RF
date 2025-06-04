from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import status, generics, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from apps.tester.filters import TestFilter, UserTestSearch
from apps.tester.models import Test, Question, Answer, UserTest
from apps.tester.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, UserTestSerializer, \
    TestSubmissionSerializer


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['test_name']


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = TestFilter


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
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['test']


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
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['QuestionId']


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
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = UserTestSearch


class SubmitTestView(APIView):

    @extend_schema(
        request=TestSubmissionSerializer,
        responses={200: dict}  # или можешь указать кастомный сериализатор для ответа
    )
    def post(self, request, test_id):
        test = get_object_or_404(Test, id=test_id)
        serializer = TestSubmissionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        user_name = serializer.validated_data['user_name']
        submitted_answers = serializer.validated_data['answers']

        correct = 0
        total = test.QuestionsCount or Question.objects.filter(test=test).count()

        for answer_data in submitted_answers:
            question_id = answer_data['question_id']
            answer_id = answer_data['answer_id']

            try:
                answer = Answer.objects.get(id=answer_id, QuestionId__id=question_id)
                if answer.IsRight:
                    correct += 1
            except Answer.DoesNotExist:
                continue

        rating = round((correct / total) * 100, 2) if total else 0.0

        UserTest.objects.create(
            ProfileId=test,
            UserName=user_name,
            Rating=rating
        )

        return Response({
            'user': user_name,
            'correct_answers': correct,
            'total_questions': total,
            'rating': rating
        })
