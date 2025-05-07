from django.urls import path

from apps.tester.views import hello

urlpatterns = [
    path('', hello, name='hello'),
]