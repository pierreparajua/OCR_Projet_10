from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from API_IssueTrackingSystem.models import Project, Contributor, Issue, Comment
from API_IssueTrackingSystem.serializers import ProjectSerializer, ContributorSerializer, \
    IssueSerializer, CommentSerializer, UsersSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributorViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        path = self.request.get_full_path()
        project_id = int([i for i in path if i.isdigit()][0])
        queryset = Issue.objects.filter(project=project_id)
        return queryset


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UsersSerializer

    def get_queryset(self):
        path = self.request.get_full_path()
        project_id = int([i for i in path if i.isdigit()][0])
        contributors = Contributor.objects.filter(project=project_id)
        users = [contributor.user for contributor in contributors]
        queryset = users
        return queryset
