import random

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from tib_backend.models import Person, Sentence
from tib_backend.serializers import PersonSerializer, SentenceSerializer


class PersonViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False)
    def randomize(self, arg):
        total_num = Person.objects.count()
        picked_pk = random.randint(0, total_num - 1)
        picked_person = Person.objects.get(pk=picked_pk)
        serializer = PersonSerializer(picked_person)
        return Response(serializer.data)


class SentenceViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False)
    def randomize(self, arg):
        total_num = Sentence.objects.count()
        picked_pk = random.randint(0, total_num - 1)
        picked_person = Sentence.objects.get(pk=picked_pk)
        serializer = SentenceSerializer(picked_person)
        return Response(serializer.data)