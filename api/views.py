from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Person
from api.serializers import PersonReviewSerializer
from rest_framework import filters


# Create your views here.

class ListApi(APIView):
    def get(self, request):
        list_review = Person.objects.all()
        serialized = PersonReviewSerializer(list_review, many=True)
        return Response(data=serialized.data)


class ListPerson(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonReviewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'fl_name', 'rooms', 'phone', 'internal_address', 'section']


class IdPerson( ):
    pass
