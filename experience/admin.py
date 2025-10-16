from django.contrib import admin
from .models import Experience, Contribution

# Register your models here.
class ContributionInline(admin.TabularInline):
    model=Contribution
    extra=1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=('job_role', 'company', 'start_period', 'end_period')
    inlines=[ContributionInline]
