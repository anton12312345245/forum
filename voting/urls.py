from django.urls import path
from voting import views

urlpatterns = [
    path("votes/", views.vote_list, name="vote-list"),
    path("votes/<int:pk>/", views.vote_detail, name="vote-detail"),
    path("votes/create/", views.vote_create, name="vote-create"),
    #path("", EditVoteView.as_view(), name="edit-vote")
]
