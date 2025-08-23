from django.urls import path
from voting import views

app_name = 'voting'

urlpatterns = [
    path("", views.vote_list, name="vote-list"),
    path("votes/<int:pk>/", views.VoteDetailView.as_view(), name="vote-detail"),
    path("votes/create/", views.VoteCreateView.as_view(), name="vote-create"),
    path("vote/edit/<int:pk>", views.EditYourVoteView.as_view(), name="edit-vote")
]
