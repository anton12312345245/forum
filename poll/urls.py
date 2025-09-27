from django.urls import path
from poll import views

app_name = 'poll'

urlpatterns = [
    path("", views.poll_list, name="poll-list"),
    path("poll/<int:pk>/", views.PollDetailView.as_view(), name="poll-detail"),
    path("polls/create/", views.PollCreateView.as_view(), name="poll-create"),
    path("poll/edit/<int:pk>", views.EditYourPollView.as_view(), name="edit-poll")
]
