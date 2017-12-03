from django.conf.urls import url
from submissions import views

urlpatterns = [
    url(r'^$', views.SubmissionsList.as_view())
]