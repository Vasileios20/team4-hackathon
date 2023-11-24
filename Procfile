web: gunicorn hack_team_4.wsgi
web: daphne hack_team_4.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=hack_team_4.settings -v2