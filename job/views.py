from multiprocessing.pool import job_counter

from django.shortcuts import render, get_object_or_404

from job.models import Job


# Create your views here.
def job_list(request):
  job_list=Job.objects.all()
  # print(job_list) ==> for debugging
  #must return 3 entities/objects
  return render(request, 'job/job_list.html', {'jobs':job_list})


def job_detail(request, job_id):
  # job = get_object_or_404(Job,pk=job_id) # this is the context
  # or
  context = {'job' : get_object_or_404(Job, pk=job_id)}
  return render(request, 'job/job_detail.html',context)