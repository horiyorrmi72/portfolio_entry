from django.db import models

# Create your models here.
class Experience(models.Model):
    company=models.CharField(max_length=255)
    job_role=models.CharField(max_length=120)
    start_period=models.DateField(help_text="joined date")
    end_period=models.DateField(help_text="end date")

    def __str__(self):
        return f"{self.job_role} at {self.company}"

class Contribution(models.Model):
    experience=models.ForeignKey(Experience,on_delete=models.CASCADE, related_name="contributions")
    description=models.TextField()

    def __str__(self):
        return self.description[:50]    