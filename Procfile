web: gunicorn team_task_manager.wsgi --log-file -
release: python manage.py migrate --no-input && python manage.py collectstatic --no-input


web: python manage.py migrate --no-input && python manage.py collectstatic --no-input && gunicorn team_task_manager.wsgi --log-file -