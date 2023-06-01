from apps.crud1_using_api_decorator.models import Student
from apps.crud1_using_api_decorator.serializers import StudentSerializer
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
