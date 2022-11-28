from rest_framework import serializers

from tib_backend.models import Person, Sentence


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'years_range_begin', 'years_range_end']


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['id', 'sentence']