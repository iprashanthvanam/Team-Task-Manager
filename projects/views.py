from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from accounts.models import User
from tasks.models import Task
from .models import Project

@login_required
def dashboard_view(request):
    user = request.user
    if user.is_admin_role:
        projects = Project.objects.all().prefetch_related('tasks')
        all_tasks = Task.objects.all().select_related('project', 'assigned_to')
    else:
        project_ids = list(user.owned_projects.values_list('id', flat=True)) + \
                      list(user.member_projects.values_list('id', flat=True))
        projects = Project.objects.filter(id__in=set(project_ids)).prefetch_related('tasks')
        all_tasks = Task.objects.filter(project__in=projects).select_related('project', 'assigned_to')

    today = timezone.now().date()
    context = {
        'projects': projects,
        'total_projects': projects.count(),
        'total_tasks': all_tasks.count(),
        'todo_tasks': all_tasks.filter(status='todo').count(),
        'inprogress_tasks': all_tasks.filter(status='in_progress').count(),
        'done_tasks': all_tasks.filter(status='done').count(),
        'overdue_tasks': all_tasks.filter(due_date__lt=today).exclude(status='done').count(),
        'recent_tasks': all_tasks.order_by('-created_at')[:5],
        'my_tasks': all_tasks.filter(assigned_to=user).exclude(status='done')[:5],
    }
    return render(request, 'dashboard.html', context)

@login_required
def project_list(request):
    user = request.user
    if user.is_admin_role:
        projects = Project.objects.all()
    else:
        owned = user.owned_projects.all()
        member = user.member_projects.all()
        projects = (owned | member).distinct()
    return render(request, 'projects/list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()
        member_ids = request.POST.getlist('members')
        if not name:
            messages.error(request, 'Project name is required.')
            return render(request, 'projects/create.html', {'users': User.objects.exclude(id=request.user.id)})
        project = Project.objects.create(name=name, description=description, owner=request.user)
        if member_ids:
            project.members.set(User.objects.filter(id__in=member_ids))
        messages.success(request, f'Project "{name}" created!')
        return redirect('project_detail', pk=project.pk)
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'projects/create.html', {'users': users})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = request.user
    if not user.is_admin_role and project.owner != user and not project.members.filter(id=user.id).exists():
        messages.error(request, 'You do not have access to this project.')
        return redirect('project_list')
    tasks = project.tasks.all().select_related('assigned_to', 'created_by')
    today = timezone.now().date()
    context = {
        'project': project,
        'tasks': tasks,
        'todo': tasks.filter(status='todo'),
        'in_progress': tasks.filter(status='in_progress'),
        'done': tasks.filter(status='done'),
        'overdue': tasks.filter(due_date__lt=today).exclude(status='done'),
        'can_manage': user.is_admin_role or project.owner == user,
    }
    return render(request, 'projects/detail.html', context)

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = request.user
    if not user.is_admin_role and project.owner != user:
        messages.error(request, 'Only Admin or project owner can edit.')
        return redirect('project_detail', pk=pk)
    if request.method == 'POST':
        project.name = request.POST.get('name', project.name).strip()
        project.description = request.POST.get('description', '').strip()
        member_ids = request.POST.getlist('members')
        project.save()
        project.members.set(User.objects.filter(id__in=member_ids))
        messages.success(request, 'Project updated.')
        return redirect('project_detail', pk=pk)
    users = User.objects.exclude(id=project.owner_id)
    return render(request, 'projects/edit.html', {'project': project, 'users': users})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    user = request.user
    if not user.is_admin_role and project.owner != user:
        messages.error(request, 'Permission denied.')
        return redirect('project_detail', pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted.')
        return redirect('project_list')
    return render(request, 'projects/confirm_delete.html', {'project': project})
