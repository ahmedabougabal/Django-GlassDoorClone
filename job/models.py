import os
import uuid

from django.db import models

JOB_TYPES = (
  ('Full Time', 'Full Time'),
  ('Part Time', 'Part Time'),
)


def image_handle(instance, filename):
  extension = filename.split('.')[-1]
  if instance.pk:
    new_filename = f'{instance.pk}.{extension}'
  else:  #if instance has no pk yet, Generate a random UUID.
    new_filename = f'{uuid.uuid4()}.{extension}'
  return os.path.join('jobs', new_filename)


# Create your models here.
class Job(models.Model):
  title = models.CharField(max_length=100)
  # location
  # job (may be either a full-time or part-time) => we use choices
  job_type = models.CharField(max_length=15, choices=JOB_TYPES)
  description = models.TextField(max_length=1000)
  published_at = models.DateTimeField(auto_now_add=True)
  vacancies = models.IntegerField(default=1)
  salary = models.IntegerField(default=0)
  experience = models.IntegerField(default=1)
  '''foreign key here 
  #since python code is executed line by line from top to bottom
   then Category must be defined in single quotes as the class Category
   comes after the class Job'''
  category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
  image = models.ImageField(upload_to=image_handle, blank=True, null=True)


  #since i need to rename the job added on my admin dashboard
  # to a name of my choice, i have to use def __str__(self)
  def __str__(self):
    return self.title


'''since it is a one-to-many relationship, job is 
associated with a specific category but a 
category contains many jobs
'''


class Category(models.Model):
  name = models.CharField(max_length=25)

  def __str__(self):
    return self.name
