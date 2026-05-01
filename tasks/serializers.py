from rest_framework import serializers
from accounts.serializers import UserSerializer
from projects.serializers import ProjectSerializer
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_detail = UserSerializer(source='assigned_to', read_only=True)
    created_by_detail = UserSerializer(source='created_by', read_only=True)
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assigned_to', 'assigned_to_detail',
                  'created_by', 'created_by_detail', 'status', 'priority', 'due_date',
                  'is_overdue', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']

    def get_is_overdue(self, obj):
        return obj.is_overdue
