from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer
from projects.models import Project

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_role:
            qs = Task.objects.all()
        else:
            owned = user.owned_projects.all()
            member = user.member_projects.all()
            projects = (owned | member).distinct()
            qs = Task.objects.filter(project__in=projects)

        # Optional filters via query params
        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        project_id = self.request.query_params.get('project')
        if status:
            qs = qs.filter(status=status)
        if priority:
            qs = qs.filter(priority=priority)
        if project_id:
            qs = qs.filter(project_id=project_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        today = timezone.now().date()
        qs = self.get_queryset().filter(due_date__lt=today).exclude(status='done')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        qs = self.get_queryset().filter(assigned_to=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
