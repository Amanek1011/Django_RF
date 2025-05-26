from django.urls import path

from apps.tester.views import hello, TestListApiView, QuestionDetailApiView

urlpatterns = [
    path('', hello, name='hello'),
    path('test',TestListApiView.as_view(),name='test-list'),
    path('question/<int:pk>',QuestionDetailApiView.as_view(),name= 'question-detail'),
]
