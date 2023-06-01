from rest_framework.response import Response
from apps.crud1_using_api_decorator.models import Student
from apps.crud1_using_api_decorator.serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        _id = pk
        if _id is not None:
            stu = Student.objects.get(id=_id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        _id = pk
        stu = Student.objects.get(pk=_id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        _id = pk
        stu = Student.objects.get(pk=_id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Data Updated"})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        _id = pk
        stu = Student.objects.get(pk=_id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
