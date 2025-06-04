from django.urls import path, include
from rest_framework import routers

from apps.tester.views import hello, TestListApiView, QuestionDetailApiView, TestDetailApiView, TestListAPIView, \
    TestViewSet, QuestionDetailAPIView, QuestionListApiView, QuestionViewSet, AnswerDetailAPIView, AnswerListApiView, \
    AnswerViewSet, UserTestDetailApiView, UserTestDetailAPIView, UserTestListApiView, UserTestViewSet, SubmitTestView

router = routers.DefaultRouter()
router.register('tests-viewset',TestViewSet)
router.register('questions-viewset',QuestionViewSet)
router.register('answers-viewset', AnswerViewSet)
router.register('users_tests-viewset', UserTestViewSet)

urlpatterns = [
    path('', hello, name='hello'),
    path('',include(router.urls)),
    #Test
    path('test', TestListApiView.as_view(), name='test-list'),
    path('generics/test/<int:pk>', TestDetailApiView.as_view(), name ='test-detail'),
    path('generics/tests-list', TestListAPIView.as_view(), name ='test-list'),
    #Question
    path('question/<int:pk>', QuestionDetailApiView.as_view(), name= 'question-detail'),
    path('generics/question/<int:pk>', QuestionDetailAPIView.as_view(), name = 'question-detail'),
    path('generics/questions-list', QuestionListApiView.as_view(), name = 'question-list'),
    #Answer
    path('answer/<int:pk>', AnswerDetailAPIView.as_view(), name = 'answer-detail'),
    path('generics/answer/<int:pk>', AnswerDetailAPIView.as_view(), name = 'answer-detail'),
    path('generics/answers-list', AnswerListApiView.as_view(), name = 'answer-list'),
    #UserTest
    path('user_test/<int:pk>', UserTestDetailApiView.as_view(), name = 'user_test-detail'),
    path('generics/user_test/<int:pk>', UserTestDetailAPIView.as_view(), name = 'user_test-detail'),
    path('generics/users_tests-list', UserTestListApiView.as_view(), name = 'user_test-list'),
    path('api/tests/<int:test_id>/submit/', SubmitTestView.as_view(), name='submit-test'),
]
