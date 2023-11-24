web: gunicorn hack_team_4.wsgi
web: daphne hack_team_4.asgi:channel_layer
worker: python manage.py runworker channel_layer -v2