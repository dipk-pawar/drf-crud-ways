from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.
@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_api(request, pk=None):
    _id = pk
    if request.method == "GET":
        if _id is not None:
            try:
                stu = Student.objects.get(id=_id)
            except Exception:
                return Response({"msg": "Sorry, Employee not found"})
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"})
        return Response(serializer.errors)

    if request.method == "PUT":
        stu = Student.objects.get(pk=_id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors)

    if request.method == "PATCH":
        stu = Student.objects.get(pk=_id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Data Updated"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        stu = Student.objects.get(pk=_id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
