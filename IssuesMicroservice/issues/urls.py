from django.urls import path
from .views import IssueListView, IssueDetailView

urlpatterns = [
    path("issues/", IssueListView.as_view(), name="issue-list"),
    path("issues/<int:pk>/", IssueDetailView.as_view(), name="issue-detail"),
]
