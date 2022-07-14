from rest_framework import routers
from API_IssueTrackingSystem.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('contributors', ContributorViewSet)
router.register('issues', IssueViewSet)
router.register('comments', CommentViewSet)
