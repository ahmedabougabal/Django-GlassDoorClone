from django.contrib import admin
from django.template.defaultfilters import title

from .models import Job, Category


# Custom admin class for Job
class JobAdmin(admin.ModelAdmin):
  list_display = ('title','vacancies', 'salary', 'experience', 'category', 'delete_image')

  # Method to display the 'Remove Image' link in the admin panel
  def delete_image(self, obj):
    if obj.image:
      return f'<a href="/admin/delete_image/{obj.id}">Remove Image</a>'
    return 'No Image'

  # Allow HTML tags to render (for older versions of Django)
  delete_image.allow_tags = True
  delete_image.short_description = 'Image Actions'  # Optional: How the column is labeled


# Register Job with the custom admin interface
admin.site.register(Job, JobAdmin)

# Register Category (assuming no custom admin changes are needed for it)
admin.site.register(Category)
