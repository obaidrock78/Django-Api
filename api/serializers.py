from rest_framework import serializers
from api.models import Person, Phone


class PersonReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'fl_name', 'rooms', 'phone', 'internal_address', 'section')


class ReviewSerializer(serializers.ModelSerializer):
    person = PersonReviewSerializer()

    class Meta:
        model = Phone
        fields = ('id', 'person_id', 'type', 'phone')
