from rest_framework import serializers

from API_IssueTrackingSystem.models import Project, Contributor, Issue, Comment


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProjectSerializers(serializers.ModelSerializer):
    #issues = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
