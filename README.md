# protein-search
celery v4.3.0; redis v5.0.5 - to queue and manage requests

django v2.2.3

biopython v1.73 (uses an api key that can be generated from your NCBI account - in 'inpform/searchseq.py')

- Start redis server: $redis-server
- Start celery worker: (venv) $ celery worker -A SearchDNA --loglevel=info
- Run application: (venv) $ python manage.py runserver

- Uses the reverse complement DNA strand sequence as input that can be pasted in the field

# Production Version

The production version of this app is hosted on Heroku: https://dnaproteinsearch.herokuapp.com/inpform/run/

It currently searches if a reverse complement DNA strand is a coding sequence in the following genomes:
['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 'NC_023640',
'NC_023719', 'NC_027867']

A future version of the application will feature a more extensive search list.
