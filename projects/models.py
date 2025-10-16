from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=80)
    category=models.CharField(max_length=50)
    project_sample_media_path = models.TextField(blank=True, null=True, help_text="Path or filename of related media")
    project_sample_url = models.URLField(blank=True, null=True, help_text="Optional link to project")

    def __str__(self):
        return self.title

class ProjectStack(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE, related_name="stacks")
    stack=models.JSONField(help_text="stack_used")

    def __str__(self):
        return self.stack