from django.shortcuts import render
from jobs.models import Job, Cities, JobTypes
from django.http import HttpResponse, Http404
from django.template import loader

from django.views import generic
# Create your views here.

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('jobs/joblist.html')
    context = {'job_list':job_list}

    for job in job_list:
        job.the_job_city = Cities[job.job_city][1]
        job.the_job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))

class JobListView(generic.ListView):
    model = Job
    context_object_name = 'newjoblist'
    template_name = 'jobs/job_list.html'

def jobdetail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404('No more Job')
    return render(request, 'jobs/job.html', {'job':job})

class JobDetailView(generic.DetailView):
    model = Job
    context_object_name = 'new_job_detail'
    template_name = 'jobs/job_detail.html'
