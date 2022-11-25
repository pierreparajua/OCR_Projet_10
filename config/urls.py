

from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from API_IssueTrackingSystem.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet)


project_router = routers.NestedDefaultRouter(router, r'projects', lookup='project')
project_router.register(r'issues', IssueViewSet, basename='issues')
project_router.register(r'users', ContributorViewSet, basename='users')

issue_router = routers.NestedDefaultRouter(project_router, r'issues', lookup='issues')
issue_router.register(r'comments', CommentViewSet, basename="comments")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', UserViewSet.as_view(), name='users'),
    path('login/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),

]
