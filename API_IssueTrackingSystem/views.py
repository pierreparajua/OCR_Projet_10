from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from API_IssueTrackingSystem.models import Project, Contributor, Issue, Comment
from API_IssueTrackingSystem.serializers import ProjectSerializer, ContributorSerializer, \
    IssueSerializer, CommentSerializer, UsersSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributorViewSet(ModelViewSet):
    serializer_class = UsersSerializer

    def get_queryset(self):
        contributors = Contributor.objects.filter(project=self.kwargs.get('project_pk'))
        users = [contributor.user for contributor in contributors]
        return users


class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.all()
        return queryset


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

