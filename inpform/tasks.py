from .searchseq import searchdna
import random

from SearchDNA.celery import celery_app
from .models import Searchstr
from django.utils import timezone


@celery_app.task(bind=True)
def returnResult(self, txt_input=None):
    b = Searchstr(search_text=txt_input, task_id=self.request.id, sub_date=timezone.now())
    b.save()
    matchLst = searchdna(txt_input)
    if len(matchLst) == 0:
        matchval = 'Sequence Not Found'
    else:
        matchval = matchLst[0]
    b.match = matchval
    b.save()

