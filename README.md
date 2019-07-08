# protein-search
celery v4.3.0; redis v5.0.5 - to queue and manage requests

django v2.2.3

biopython v1.73 (uses an api key that can be generated from your NCBI account)

- Start redis server: $redis-server
- Start celery worker: (venv) $ celery worker -A SearchDNA --loglevel=info
- Run application: (venv) $ python manage.py runserver

http://127.0.0.1:8000/inpform/run/
