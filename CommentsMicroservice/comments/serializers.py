from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    issueId = serializers.IntegerField()
    profileId = serializers.IntegerField()
    message = serializers.CharField()
