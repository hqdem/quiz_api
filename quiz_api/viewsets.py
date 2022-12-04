from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Topic, Test, Question, Option
from .serializers import TopicSerializer, TestSerializer, QuestionSerializer, OptionSerializer
from .permissons import IsAdminOrReadOnly


class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAdminOrReadOnly]


class TestViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Test.objects.all()
        test = get_object_or_404(queryset, pk=pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)


class QuestionViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class OptionViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Option.objects.all()
        serializer = OptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Option.objects.all()
        option = get_object_or_404(queryset, pk=pk)
        serializer = OptionSerializer(option)
        return Response(serializer.data)
