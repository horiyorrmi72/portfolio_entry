from django.contrib import admin
from .models import Project, ProjectStack

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","category","get_stack")

    def get_stack(self, obj):
            return ", ".join(
                   [", ".join(stack.stack) if isinstance(stack.stack, list) else str(stack.stack) for stack in obj.stacks.all()]
                     )
