from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_role:
            return Project.objects.all()
        owned = user.owned_projects.all()
        member = user.member_projects.all()
        return (owned | member).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        project = self.get_object()
        if not request.user.is_admin_role and project.owner != request.user:
            return Response({'detail': 'Permission denied.'}, status=403)
        user_id = request.data.get('user_id')
        from accounts.models import User
        try:
            user = User.objects.get(id=user_id)
            project.members.add(user)
            return Response({'detail': f'{user.username} added to project.'})
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=404)
