from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from accounts.models import User
from projects.models import Project
from .models import Task

def get_user_projects(user):
    if user.is_admin_role:
        return Project.objects.all()
    owned = user.owned_projects.all()
    member = user.member_projects.all()
    return (owned | member).distinct()

@login_required
def task_list(request):
    user = request.user
    projects = get_user_projects(user)
    tasks = Task.objects.filter(project__in=projects).select_related('project', 'assigned_to', 'created_by')

    # Filters
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    project_filter = request.GET.get('project', '')
    mine_only = request.GET.get('mine', '')

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    if project_filter:
        tasks = tasks.filter(project_id=project_filter)
    if mine_only:
        tasks = tasks.filter(assigned_to=user)

    context = {
        'tasks': tasks,
        'projects': projects,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'project_filter': project_filter,
        'mine_only': mine_only,
        'today': timezone.now().date(),
    }
    return render(request, 'tasks/list.html', context)

@login_required
def task_create(request):
    user = request.user
    projects = get_user_projects(user)
    project_id = request.GET.get('project', '')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        project_id = request.POST.get('project', '')
        assigned_to_id = request.POST.get('assigned_to', '')
        status = request.POST.get('status', 'todo')
        priority = request.POST.get('priority', 'medium')
        due_date = request.POST.get('due_date', '') or None

        if not title or not project_id:
            messages.error(request, 'Title and Project are required.')
            return render(request, 'tasks/create.html', {
                'projects': projects,
                'users': User.objects.all(),
                'selected_project': project_id,
            })

        project = get_object_or_404(Project, pk=project_id)
        assigned_to = User.objects.filter(id=assigned_to_id).first() if assigned_to_id else None

        task = Task.objects.create(
            title=title, description=description, project=project,
            assigned_to=assigned_to, created_by=user, status=status,
            priority=priority, due_date=due_date
        )
        messages.success(request, f'Task "{title}" created!')
        return redirect('task_detail', pk=task.pk)

    context = {
        'projects': projects,
        'users': User.objects.all(),
        'selected_project': project_id,
    }
    return render(request, 'tasks/create.html', context)

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    user = request.user
    projects = get_user_projects(user)
    if task.project not in projects:
        messages.error(request, 'Access denied.')
        return redirect('task_list')
    can_manage = user.is_admin_role or task.project.owner == user or task.created_by == user
    return render(request, 'tasks/detail.html', {
        'task': task,
        'can_manage': can_manage,
        'today': timezone.now().date(),
    })

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    user = request.user
    projects = get_user_projects(user)
    can_manage = user.is_admin_role or task.project.owner == user or task.created_by == user
    if not can_manage and task.assigned_to != user:
        messages.error(request, 'Permission denied.')
        return redirect('task_detail', pk=pk)

    if request.method == 'POST':
        task.title = request.POST.get('title', task.title).strip()
        task.description = request.POST.get('description', '').strip()
        task.status = request.POST.get('status', task.status)
        task.priority = request.POST.get('priority', task.priority)
        task.due_date = request.POST.get('due_date', '') or None
        if can_manage:
            assigned_id = request.POST.get('assigned_to', '')
            task.assigned_to = User.objects.filter(id=assigned_id).first() if assigned_id else None
        task.save()
        messages.success(request, 'Task updated.')
        return redirect('task_detail', pk=pk)

    context = {
        'task': task,
        'projects': projects,
        'users': task.project.get_all_members(),
        'can_manage': can_manage,
    }
    return render(request, 'tasks/edit.html', context)

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    user = request.user
    if not user.is_admin_role and task.project.owner != user and task.created_by != user:
        messages.error(request, 'Permission denied.')
        return redirect('task_detail', pk=pk)
    project_pk = task.project.pk
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('project_detail', pk=project_pk)
    return render(request, 'tasks/confirm_delete.html', {'task': task})

@login_required
def task_status_update(request, pk):
    """Quick status toggle via POST"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status', task.status)
        task.status = new_status
        task.save(update_fields=['status', 'updated_at'])
        messages.success(request, f'Status updated to {task.get_status_display()}.')
    return redirect(request.META.get('HTTP_REFERER', 'task_list'))
