import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from .serializers import CommentSerializer

BASE_URL = settings.COMMENTS_API_URL


class CommentListView(APIView):

    @extend_schema(
        summary="List all comments",
        responses={200: CommentSerializer(many=True)},
    )
    def get(self, request):
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        serializer = CommentSerializer(data=response.json(), many=True)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDetailView(APIView):

    @extend_schema(
        summary="Retrieve a comment by ID",
        parameters=[
            OpenApiParameter(
                "id", OpenApiTypes.INT, OpenApiParameter.PATH, description="Comment ID"
            )
        ],
        responses={200: CommentSerializer, 404: None},
    )
    def get(self, request, pk):
        response = requests.get(f"{BASE_URL}/{pk}", timeout=10)
        if response.status_code == 404:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        response.raise_for_status()
        serializer = CommentSerializer(data=response.json())
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
