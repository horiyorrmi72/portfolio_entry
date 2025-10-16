from django.urls import path
from .views import ExperienceListView

urlpatterns=[
    path("",ExperienceListView.as_view(),name="list_experience")
]