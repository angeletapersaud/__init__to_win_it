from rest_framework import serializers


class IssueSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    projectId = serializers.IntegerField()
    assigneeProfileId = serializers.IntegerField()
    summary = serializers.CharField(max_length=255)
    status = serializers.CharField(max_length=50)
    priority = serializers.CharField(max_length=50)
