from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    key = serializers.CharField(max_length=10)
    leadProfileId = serializers.IntegerField()
