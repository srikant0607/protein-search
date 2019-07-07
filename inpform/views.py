# Views for inpform

from django.shortcuts import render
from .tasks import returnResult
from .models import Searchstr
from django.views.decorators.http import require_http_methods, require_GET
from .forms import NameForm
from celery.result import AsyncResult


@require_http_methods(["GET", "POST"])
def run(request):
    if request.method == "POST":
        form = NameForm(request.POST)

        if form.is_valid():
            txt_input = form.cleaned_data['txt_input']
            returnResult.delay(txt_input=txt_input)

            return render(request, 'inpform/job.html', context={'form': NameForm, 'message': 'Search Underway...'})

    else:
        return render(request, 'inpform/job.html', context={'form': NameForm})


def track_jobs():
    entries = Searchstr.objects.all()
    information = []
    for item in entries:
        progress = 100  # max value for bootstrap progress bar, when the job is finished
        result = AsyncResult(item.task_id)
        match = item.match

        if isinstance(result.info, dict):
            progress = result.info['progress']
        information.append([match, result.state, progress, item.id])
    return information


@require_GET
def monitor(request):
    info = track_jobs()
    return render(request, 'inpform/monitor.html', context={'info': info})


