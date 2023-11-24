web: gunicorn hack_team_4.wsgi
web: daphne hack_team_4.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2