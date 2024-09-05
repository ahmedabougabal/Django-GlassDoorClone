from django.db import models

JOB_TYPES = (
  ('Full Time','Full Time'),
  ('Part Time','Part Time'),
)

# Create your models here.
class Job(models.Model):
  title = models.CharField(max_length=100)
  # location
  # job (may be either a full-time or part-time) => we use choices
  job_type = models.CharField(max_length=15, choices=JOB_TYPES)
  description = models.TextField(max_length=1000)
  published_at = models.DateTimeField(auto_now_add=True)
  vacancies=models.IntegerField(default=1)
  salary = models.IntegerField(default=0)
  experience = models.IntegerField(default=1)

  #since i need to rename the job added on my admin dashboard
  # to a name of my choice, i have to use def __str__(self)
  def __str__(self):
    return self.title