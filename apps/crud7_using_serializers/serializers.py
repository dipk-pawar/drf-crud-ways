from rest_framework import serializers
from apps.crud1_using_api_decorator.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        import pdb

        pdb.set_trace()
        print("--------------------------------------")
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.title)
        instance.roll = validated_data.get("roll", instance.roll)
        instance.city = validated_data.get("city", instance.city)
        instance.save()
        return instance
